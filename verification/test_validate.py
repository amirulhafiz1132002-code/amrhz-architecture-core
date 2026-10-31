import contextlib
import io
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

import validate


NOW = "2026-11-01T00:00:00Z"
SHA = "a" * 40


def project_record(state="VERIFIED", previous="DEVELOPMENT", evidence_type="test_result"):
    return {
        "schema_version": "2.0.0",
        "project": {
            "repository": "owner/repo",
            "ref": "feature/test",
            "commit_sha": SHA
        },
        "scope": "validator unit test",
        "state": state,
        "previous_state": previous,
        "claim": "The scoped validation claim was tested.",
        "evidence": [{
            "type": evidence_type,
            "reference": "https://example.invalid/evidence/1",
            "observed_at": NOW,
            "supports": "A deterministic test result"
        }],
        "updated_at": NOW
    }


class GovernanceSchemaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.project_schema = validate.load_json(validate.SCHEMA_DIR / "project-state.schema.json")
        cls.doc_schema = validate.load_json(validate.SCHEMA_DIR / "doc-lifecycle.schema.json")
        cls.project_validator = Draft202012Validator(cls.project_schema, format_checker=FormatChecker())
        cls.doc_validator = Draft202012Validator(cls.doc_schema, format_checker=FormatChecker())

    def test_verified_requires_revision_and_test_evidence(self):
        record = project_record()
        self.assertEqual(list(self.project_validator.iter_errors(record)), [])
        del record["project"]["commit_sha"]
        self.assertNotEqual(list(self.project_validator.iter_errors(record)), [])

    def test_live_requires_deployment_evidence(self):
        record = project_record(state="LIVE", previous="VERIFIED", evidence_type="test_result")
        self.assertNotEqual(list(self.project_validator.iter_errors(record)), [])
        record["evidence"][0]["type"] = "deployment_record"
        self.assertEqual(list(self.project_validator.iter_errors(record)), [])

    def test_initial_document_must_be_draft(self):
        record = {
            "schema_version": "1.0.0",
            "document": "README.md",
            "revision_sha": SHA,
            "lifecycle": "DRAFT",
            "previous_lifecycle": None,
            "updated_at": NOW,
            "evidence": [{
                "type": "commit",
                "reference": SHA,
                "description": "Initial document revision"
            }]
        }
        self.assertEqual(list(self.doc_validator.iter_errors(record)), [])
        record["lifecycle"] = "APPROVED"
        self.assertNotEqual(list(self.doc_validator.iter_errors(record)), [])

    def test_project_transition_rejects_skipping_to_live(self):
        record = project_record(state="LIVE", previous="DEVELOPMENT", evidence_type="deployment_record")
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = validate.validate_project_transition(record, "unit-test")
        self.assertEqual(result, 1)
        self.assertIn("disallowed project transition", output.getvalue())

    def test_document_transition_requires_review_before_approval(self):
        record = {
            "document": "README.md",
            "revision_sha": SHA,
            "lifecycle": "APPROVED",
            "previous_lifecycle": "DRAFT",
            "approval": {
                "decision": "APPROVE",
                "document": "README.md",
                "revision_sha": SHA
            }
        }
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = validate.validate_document_transition(record, "unit-test")
        self.assertEqual(result, 1)
        self.assertIn("approval must follow REVIEWED", output.getvalue())


if __name__ == "__main__":
    unittest.main()
