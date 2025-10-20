<!--
Sync Impact Report
- Version change: 1.0.0 → 1.1.0
- Modified principles: Template-Aligned Delivery → Incremental Template Delivery
- Added principles: VI. PEP 8 Craftsmanship; VII. Kid-Friendly Clarity
- Added sections: None
- Removed sections: None
- Templates requiring updates: ✅ .specify/templates/plan-template.md; ✅ .specify/templates/spec-template.md; ✅ .specify/templates/tasks-template.md; ⚠ .specify/templates/commands/*.md (directory absent — create guidance when commands are introduced)
- Follow-up TODOs: None
-->

# Pycraft Constitution

## Core Principles

### I. Library-First Modularity
- Feature logic MUST live in importable packages under `src/pycraft/` (create the package structure when absent).
- CLI adapters in `cli/` MUST only orchestrate library calls; no business rules live in entrypoints.
- Every new or modified module MUST include top-level docstrings describing purpose, inputs, and side effects.
Rationale: A clean separation between libraries and adapters keeps the codebase reusable, testable, and predictable.

### II. CLI Contract Fidelity
- Each capability MUST expose a CLI command with deterministic text I/O (stdin/args → stdout, errors → stderr).
- Commands MUST provide a `--json` flag that emits machine-readable output matching the documented schema.
- Exit codes MUST distinguish success (0) from categorized failures (>0) with actionable stderr messaging.
Rationale: Reliable CLI contracts enable automation, scripting, and reproducible debugging.

### III. Test-Driven Proof
- Tests covering new behavior MUST be authored before implementation and observed failing prior to code changes.
- Unit tests belong in `tests/unit/`, integration flows in `tests/integration/`, and cross-contract assertions in `tests/contract/`.
- Every user story accepted into a release MUST own at least one automated acceptance test.
Rationale: Enforcing red-green cycles turns specifications into living executable guarantees.

### IV. Traceable Observability
- Logging MUST use Python’s `logging` module (or compatible adapters) with structured key/value context.
- Errors MUST include module name, failing operation, and remediation hint; no silent exception swallowing.
- Each CLI command MUST accept `--verbose` to elevate log level and surface diagnostic insights.
Rationale: Traceable signals make failures debuggable under real operational pressure.

### V. Incremental Template Delivery
- Work MUST progress through `spec` → `plan` → `tasks` before application code merges.
- Constitution Check sections MUST confirm principles I–IV are satisfied or document time-bound exceptions.
- Tasks MUST remain independently testable slices that specify exact file paths they will touch.
Rationale: Template discipline keeps delivery incremental, auditable, and reversible.

### VI. PEP 8 Craftsmanship
- Code MUST compile with `uv run ruff check` and `uv run ruff format` (or equivalent black/ruff tooling) before review.
- All modules MUST include type hints, descriptive names, and docstrings that reflect current behavior.
- Dependencies MUST be modern Pythonic choices (dataclasses, pathlib, f-strings) unless compatibility constraints are documented.
Rationale: PEP 8-aligned craftsmanship and modern idioms keep the codebase healthy and future-ready.

### VII. Kid-Friendly Clarity
- Functions, classes, and variables MUST use everyday language that a 12-year-old can follow without jargon.
- Each logic block MUST carry a one-sentence comment explaining the intent in plain speech.
- README and sample code MUST include short stories or analogies when introducing new ideas.
Rationale: Teaching-level clarity widens contributor access and reveals hidden complexity early.

## Technical Guardrails

- Language baseline: Python 3.12; deviations require governance approval and documented compatibility plans.
- Dependencies MUST be declared in `pyproject.toml` (or equivalent) with caret (^) version ranges and lockfiles committed.
- Environment configuration MUST flow through `.env.example` documentation; secrets stay out of version control.
- Local data artifacts belong under `data/` with README coverage; remote integrations demand explicit security review.
- Dependency management MUST use `uv` (project initialized via `uv init`, installs via `uv add`, locking via `uv export --locked`).

## Delivery Workflow

1. Capture user intent in `/specs/[feature]/spec.md`, documenting CLI contracts, library touchpoints, and acceptance tests.
2. Generate `/speckit.plan` output and complete the plan template, satisfying the Constitution Check gate before Phase 0 research.
3. Populate `plan.md` with architecture, dependencies, and testing approach, then produce `tasks.md` that sequences tests before implementation.
4. Maintain compliance logs (exceptions, waivers, follow-ups) in repository docs until remediated and reviewed.
5. Demonstrate the feature with a narrative walkthrough suitable for young learners, highlighting comments that explain the story.

## Governance

- Amendments require a PR that updates this constitution, documents the rationale, and references affected templates or processes.
- Versioning follows semantic rules: MAJOR for breaking or removed principles, MINOR for new principles/sections, PATCH for clarifications.
- Compliance reviews run at minimum during `/speckit.plan`, before merge, and prior to release; findings MUST note owner and due date.
- Temporary exceptions MUST include `TODO(owner, due_date, reason)` annotations and appear in follow-up tracking until resolved.

**Version**: 1.1.0 | **Ratified**: 2025-10-20 | **Last Amended**: 2025-10-20
