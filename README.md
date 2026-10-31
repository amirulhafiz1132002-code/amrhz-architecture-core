# AMRHZ Architecture Core

> Facilitating seamless collaboration between HUMAN and AI in system development

## 🎯 Project Vision

AMRHZ Architecture Core is a foundational framework designed to enable effective collaboration between human developers and AI systems. This repository documents structural components, integration points, and operating principles for further development and adaptation.

## 📋 Table of Contents

- [Overview](#overview)
- [Core Components](#core-components)
- [Architecture Layers](#architecture-layers)
- [Integration Points](#integration-points)
- [Web Development Stack](#web-development-stack)
- [Governance Standards](#governance-standards)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

## 🏗️ Overview

The architecture follows Human-AI Collaboration:
- **Humans** contribute strategic thinking, domain expertise, constraints, and final decisions.
- **AI** assists with reasoning, architecture, implementation, and verification.
- **Machine/runtime** supplies observable repository, test, API, log, and deployment evidence.

## 🔧 Core Components

- System design patterns and architectural decisions.
- Data flow and state management.
- Module organization and dependencies.
- AI-assisted development workflows and human decision checkpoints.
- External service integration boundaries.

## 🏢 Architecture Layers

```
┌─────────────────────────────────────────────────────┐
│              Presentation Layer (UI/UX)             │
├─────────────────────────────────────────────────────┤
│         Business Logic & Application Layer          │
├─────────────────────────────────────────────────────┤
│           Data Access & Integration Layer           │
├─────────────────────────────────────────────────────┤
│        Core Infrastructure & Platform Layer         │
└─────────────────────────────────────────────────────┘
```

## 🧭 Governance Standards

The governance baseline is documented in the [standards index](docs/standards/README.md). It includes:
- UI evolution and preservation rules.
- Dual-layer human and AI-oriented documentation.
- Evidence-backed project state and verification records.
- Independent project and documentation lifecycles.
- RWCAI role separation and explicit human approval gates.

**Status:** Governance changes in the RWCAI implementation branch are proposed for review. The validator and CI workflow are intended to provide structural checks; they do not by themselves authenticate approval events or enforce branch protection. See the [compliance matrix](docs/asip-13/compliance-matrix.md) for the current evidence boundary.

## 🚀 Getting Started

### Prerequisites
- Git
- Python 3.12 for governance validation

### Installation
```bash
git clone https://github.com/amirulhafiz1132002-code/amrhz-architecture-core.git
cd amrhz-architecture-core
```

### Governance validation
```bash
python -m pip install "jsonschema>=4.23,<5"
python -m py_compile verification/validate.py
python verification/validate.py
```

## 🤝 Contributing

1. Create a feature branch from main.
2. Inspect the current baseline and define the change boundary.
3. Implement the smallest evidence-backed change.
4. Run tests and include observed evidence in the pull request.
5. Request independent review where required.
6. Merge only after the repository owner approves.

## 📝 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
