# AMRHZ AI–Machine Collaboration Architecture

> A development architecture for structured interaction between a human, AI systems, and the machine/runtime environment.

## 1. Purpose

This document defines the collaboration layer for AMRHZ Architecture Core / AP1.

The objective is not to make AI appear autonomous. The objective is to create a traceable collaboration loop where:

**Human ↔ AI ↔ Machine/System**

can exchange context, questions, evidence, decisions, execution results, and checkpoints during system architecture development.

## 2. Core Principle

> **REAL STATE > UI SIMULATION**

The collaboration layer MUST NOT invent activity, memory, execution, system health, or project state.

Every important system claim should be traceable to one or more of:

- user input
- repository/source code
- runtime state
- tool execution result
- test result
- stored project checkpoint
- explicitly recorded architectural decision

## 3. Collaboration Actors

### Human

Provides:

- intent
- architectural direction
- constraints
- approval/rejection
- domain knowledge
- final decisions for consequential changes

### AI

Provides:

- reasoning assistance
- architecture proposals
- code analysis
- interrogation/questions
- consistency checks
- implementation assistance
- test interpretation
- documentation/checkpoint generation

AI MUST distinguish between facts, retrieved context, inference, proposal, and execution result.

### Machine / Runtime

Provides observable evidence:

- filesystem/repository state
- runtime state
- API responses
- logs
- test output
- deployment state
- health/diagnostic signals

The machine is the evidence layer, not merely a passive execution target.

## 4. Collaboration Loop

```text
┌──────────────┐
│    HUMAN     │
│ Intent/Goal  │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│      AI      │
│ Understand   │
│ Interrogate  │
│ Propose      │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│   MACHINE    │
│ Inspect      │
│ Execute      │
│ Measure      │
└──────┬───────┘
       │ evidence
       ▼
┌──────────────┐
│      AI      │
│ Analyze      │
│ Validate     │
│ Report       │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│    HUMAN     │
│ Review       │
│ Decide       │
└──────────────┘
```

This loop can repeat for every architectural task.

## 5. Interrogation Protocol

AI should actively ask structured questions when required information is missing.

Examples:

- What is the intended system state?
- Which repository/module is authoritative?
- Is this a design proposal or an implemented feature?
- What evidence confirms the current state?
- What constraints must remain unchanged?
- What should happen if the operation fails?
- Does this decision affect memory, identity, security, or runtime state?

The purpose of interrogation is to reduce ambiguity before implementation.

## 6. Interaction Object

A collaboration event SHOULD be representable as a structured object:

```json
{
  "interaction_id": "int_...",
  "actor": "human | ai | machine",
  "action": "intent | question | proposal | inspection | execution | evidence | decision | checkpoint",
  "session_id": "sess_...",
  "project_id": "proj_...",
  "timestamp": "ISO-8601",
  "input": {},
  "output": {},
  "evidence_refs": [],
  "status": "pending | approved | rejected | executed | failed",
  "confidence": 0.0
}
```

This object represents an interaction event. It is NOT the long-term memory database itself.

## 7. Context Envelope

A `UserContextObject` may be used as a lightweight context envelope for a request.

It should identify the current user/session/project context without carrying the entire historical memory store.

Conceptual separation:

```text
UserContextObject
        │
        ├── Identity context
        ├── Profile/preferences
        ├── Active project
        └── Session context
                │
                ▼
        Retrieval Layer
                │
        ┌───────┴────────┐
        ▼                ▼
 Persistent Memory   Project State
```

## 8. Persistent Memory Boundary

Long-term memory MUST be stored separately from transient request context.

A memory record should preserve at least:

- memory identifier
- user scope
- project scope where applicable
- memory type
- content
- source/evidence reference
- created/updated timestamps
- confidence
- importance
- lifecycle status

Memory retrieval should be selective. Relevant memory is retrieved; the entire history is not blindly injected into every request.

## 9. State Management

The architecture distinguishes:

1. **Identity State** — who is authenticated/authorized
2. **Session State** — what is happening in the current interaction
3. **Project State** — current development state
4. **Runtime State** — what the machine is actually doing
5. **Memory State** — durable knowledge and checkpoints
6. **Decision State** — accepted/rejected architectural decisions

Authentication MUST NOT be treated as proof that every stored memory should be loaded.

Authorization controls access; retrieval controls relevance.

## 10. Development Lifecycle

AMRHZ/AP1 development follows an observable progression:

```text
HEALTH
  ↓
DIAGNOSTICS
  ↓
MISSIONS
  ↓
AGENT EXECUTION
  ↓
EVALUATION
  ↓
LEARNING
```

The collaboration layer supports each stage but does not claim a stage has occurred without evidence.

## 11. One Task → Test → PASS → Next

Development operations SHOULD follow this sequence:

```text
Understand
   ↓
Inspect existing state
   ↓
Define one task
   ↓
Implement
   ↓
Test
   ↓
PASS / FAIL
   ↓
Record evidence
   ↓
Checkpoint
   ↓
Next task
```

This prevents architectural drift and makes AI-assisted development recoverable.

## 12. Architectural Safety Rules

- No fake activity.
- No invented memory.
- No false status.
- No hidden execution.
- No untraceable memory.
- No autonomous claims without observable evidence.
- No secrets stored as ordinary memory.
- No unnecessary infrastructure before the state model is clear.
- Human approval remains explicit for consequential architectural decisions.

## 13. Initial Implementation Scope

This document is an architecture checkpoint, not a claim that the complete collaboration engine already exists.

Recommended implementation order:

1. Define collaboration event schema.
2. Define session/project state schema.
3. Add observable inspection/evidence records.
4. Add memory records and retrieval interfaces.
5. Add AI interrogation workflow.
6. Add execution/evaluation loop.
7. Add learning only after the previous layers are observable and reliable.

## 14. Design Goal

The final system should allow an individual developer and AI systems to collaborate as a structured engineering process:

**Intent → Interrogation → Context → Proposal → Machine Evidence → Evaluation → Human Decision → Checkpoint → Memory**

The goal is not AI consciousness or simulated autonomy.

The goal is a reliable architecture in which human intent, AI assistance, and machine state remain connected, observable, and recoverable.
