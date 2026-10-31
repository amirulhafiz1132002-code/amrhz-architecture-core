#!/usr/bin/env python3
"""Validate AMRHZ governance schemas and repository records.

This tool checks structural validity and selected cross-record invariants.
It does not authenticate humans, prove evidence is truthful, or verify remote
deployment state. Those claims require independent inspection.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import urlparse

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"
RECORD_DIRS = {
    "project-state": (ROOT / "records" / "project-state", "project-state.schema.json"),
    "verification": (ROOT / "records" / "verification", "verification-record.schema.json"),
    "document-lifecycle": (ROOT / "records" / "document-lifecycle", "doc-lifecycle.schema.json"),
    "approvals": (ROOT / "records" / "approvals", "approval-record.schema.json"),
}

PROJECT_TRANSITIONS = {
    "CONCEPT": {"PROPOSED", "BLOCKED", "UNKNOWN"},
    "PROPOSED": {"PLANNED", "CONCEPT", "BLOCKED", "UNKNOWN"},
    "PLANNED": {"DEVELOPMENT", "PROPOSED", "BLOCKED", "UNKNOWN"},
    "DEVELOPMENT": {"PARTIAL", "VERIFIED", "BLOCKED", "UNKNOWN"},
    "PARTIAL": {"DEVELOPMENT", "VERIFIED", "BLOCKED", "UNKNOWN"},
    "VERIFIED": {"DEVELOPMENT", "PARTIAL", "LIVE", "BLOCKED", "UNKNOWN"},
    "LIVE": {"DEVELOPMENT", "BLOCKED", "UNKNOWN"},
    "BLOCKED": {"CONCEPT", "PROPOSED", "PLANNED", "DEVELOPMENT", "PARTIAL", "VERIFIED", "LIVE", "UNKNOWN"},
    "UNKNOWN": {"CONCEPT", "PROPOSED", "PLANNED", "DEVELOPMENT", "PARTIAL", "VERIFIED", "LIVE", "BLOCKED"},
}
DOC_TRANSITIONS = {
    "DRAFT": {"REVIEWED"},
    "REVIEWED": {"APPROVED", "DRAFT"},
    "APPROVED": {"DEPRECATED"},
    "DEPRECATED": set(),
}


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def report_schema_errors(instance, validator, label):
    errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.absolute_path))
    for error in errors:
        location = ".".join(str(part) for part in error.absolute_path) or "<root>"
        print(f"FAIL {label}:{location}: {error.message}")
    return len(errors)


def git_blob_sha(path: Path) -> str:
    content = path.read_bytes()
    header = f"blob {len(content)}\0".encode("utf-8")
    return hashlib.sha1(header + content).hexdigest()


def validate_project_transition(record, label):
    previous = record.get("previous_state")
    current = record.get("state")
    if previous is None:
        if current not in {"CONCEPT", "PROPOSED", "UNKNOWN"}:
            print(f"FAIL {label}: initial previous_state=null is not valid for state={current}")
            return 1
        return 0
    if current != previous and current not in PROJECT_TRANSITIONS.get(previous, set()):
        print(f"FAIL {label}: disallowed project transition {previous} -> {current}")
        return 1
    return 0


def validate_document_transition(record, label):
    previous = record.get("previous_lifecycle")
    current = record.get("lifecycle")
    if previous is None:
        if current != "DRAFT":
            print(f"FAIL {label}: an initial document lifecycle must be DRAFT")
            return 1
    elif current != previous and current not in DOC_TRANSITIONS.get(previous, set()):
        print(f"FAIL {label}: disallowed document transition {previous} -> {current}")
        return 1

    approval = record.get("approval")
    if current == "APPROVED":
        if not approval:
            print(f"FAIL {label}: APPROVED requires a traceable approval record")
            return 1
        if approval.get("decision") != "APPROVE":
            print(f"FAIL {label}: approval decision must be APPROVE")
            return 1
        if approval.get("document") != record.get("document"):
            print(f"FAIL {label}: approval document does not match lifecycle record")
            return 1
        if approval.get("revision_sha", "").lower() != record.get("revision_sha", "").lower():
            print(f"FAIL {label}: approval revision does not match document revision")
            return 1
        if previous != "REVIEWED":
            print(f"FAIL {label}: approval must follow REVIEWED")
            return 1

    document = record.get("document")
    revision = record.get("revision_sha")
    if document and revision:
        candidate = (ROOT / document).resolve()
        if not candidate.is_relative_to(ROOT) or not candidate.is_file():
            print(f"FAIL {label}: document path is missing or escapes the repository: {document}")
            return 1
        if git_blob_sha(candidate).lower() != revision.lower():
            print(f"FAIL {label}: revision_sha does not match the current Git blob for {document}")
            return 1
    return 0


def validate_evidence_references(record, label):
    errors = 0
    evidence_items = record.get("evidence", [])
    for index, item in enumerate(evidence_items):
        if item.get("type") != "source_file":
            continue
        reference = item.get("reference", "")
        parsed = urlparse(reference)
        if parsed.scheme in {"http", "https"}:
            continue
        rel = PurePosixPath(reference)
        candidate = (ROOT / Path(*rel.parts)).resolve()
        if rel.is_absolute() or ".." in rel.parts or not candidate.is_relative_to(ROOT) or not candidate.is_file():
            print(f"FAIL {label}: evidence[{index}] source_file reference is not a repository file or URL: {reference}")
            errors += 1
    return errors


def main() -> int:
    errors = 0
    schema_validators = {}
    schema_names = [
        "project-state.schema.json",
        "verification-record.schema.json",
        "doc-lifecycle.schema.json",
        "approval-record.schema.json",
    ]

    for name in schema_names:
        path = SCHEMA_DIR / name
        try:
            schema = load_json(path)
            Draft202012Validator.check_schema(schema)
            schema_validators[name] = Draft202012Validator(schema, format_checker=FormatChecker())
            print(f"PASS schema {name}")
        except Exception as exc:  # report malformed JSON and invalid schemas clearly
            print(f"FAIL schema {name}: {exc}")
            errors += 1

    records_found = 0
    for category, (directory, schema_name) in RECORD_DIRS.items():
        if schema_name not in schema_validators or not directory.exists():
            continue
        for path in sorted(directory.glob("*.json")):
            records_found += 1
            label = path.relative_to(ROOT).as_posix()
            try:
                record = load_json(path)
            except Exception as exc:
                print(f"FAIL {label}: invalid JSON: {exc}")
                errors += 1
                continue

            before = errors
            errors += report_schema_errors(record, schema_validators[schema_name], label)
            if category == "project-state":
                errors += validate_project_transition(record, label)
                if record.get("state") == "VERIFIED" and not record.get("project", {}).get("commit_sha"):
                    print(f"FAIL {label}: VERIFIED requires project.commit_sha")
                    errors += 1
                if record.get("state") == "LIVE" and not record.get("project", {}).get("commit_sha"):
                    print(f"FAIL {label}: LIVE requires project.commit_sha")
                    errors += 1
            elif category == "document-lifecycle":
                errors += validate_document_transition(record, label)
            elif category == "verification":
                if record.get("result") == "PASS" and not record.get("commit_sha"):
                    print(f"FAIL {label}: PASS requires commit_sha")
                    errors += 1
            errors += validate_evidence_references(record, label)
            if errors == before:
                print(f"PASS record {label}")

    if records_found == 0:
        print("INFO no record instances found; schema validation completed without inventing project state")

    if errors:
        print(f"RESULT FAIL: {errors} validation error(s)")
        return 1
    print("RESULT PASS: governance schemas and discovered records are structurally valid")
    print("LIMITATION: this validator does not authenticate approval events or prove evidence truth")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
