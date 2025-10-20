# Implementation Plan: Ursina Minecraft Clone

**Branch**: `001-ursina-craft` | **Date**: 2025-10-20 | **Spec**: `/specs/001-ursina-craft/spec.md`
**Input**: Feature specification from `/specs/001-ursina-craft/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Build a UV-managed Python 3.12 game that recreates a friendly Minecraft-style experience using Ursina, layered modules (UI, gameplay, world, physics), and CLI tooling with JSON output. Gameplay must feel approachable to 12-year-olds, with pytest coverage, PEP 8 compliance via ruff/black, and save/load persistence.

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->

**Language/Version**: Python 3.12  
**Primary Dependencies**: Ursina engine, uv package manager, ruff, black, pytest, mypy  
**Storage**: Local file-based world slots under `slots/` (consider JSON or binary chunk serialization)  
**Testing**: pytest with unit, integration, and contract suites orchestrated via `uv run pytest`  
**Target Platform**: Desktop (macOS, Windows, Linux) with GPU capable of running Ursina (OpenGL)  
**Project Type**: Single project (CLI + libraries under `src/pycraft/`)  
**Performance Goals**: Maintain ≥30 FPS in a 16×16×32 block scene; CLI commands respond <2s  
**Constraints**: Code and comments must remain understandable to 12-year-olds; CLI must support `--json`; layered architecture MUST separate UI/gameplay/world/physics  
**Scale/Scope**: Single-player sandbox with one overworld, up to 3 save slots, no networking

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Principle I — Library-First Modularity**: Core logic will reside under `src/pycraft/` modules (`app`, `gameplay`, `world`, `physics`, `ui`); CLI entrypoints in `cli/pycraft.py` only orchestrate runs.
- **Principle II — CLI Contract Fidelity**: CLI commands (`pycraft play`, `pycraft manage`) will expose documented args (`--mode`, `--load`, `--json`) with deterministic stdout/stderr and exit codes (11/12/21/31/32).
- **Principle III — Test-Driven Proof**: Tests to fail first: `tests/unit/test_world_generation.py::test_flat_world_height`, `tests/unit/test_block_manager.py::test_add_remove`, `tests/integration/test_cli_play.py::test_play_command_json`, `tests/contract/test_save_load.py::test_latest_slot_roundtrip`.
- **Principle IV — Traceable Observability**: Use `logging` with structured context (`event=world_generated`, `slot=latest`); `--verbose` toggles DEBUG level; errors include module + remediation (e.g., "update GPU driver").
- **Principle V — Incremental Template Delivery**: Spec complete; plan + research + data model + contracts + quickstart delivered before coding; tasks will reference exact files per story.
- **Principle VI — PEP 8 Craftsmanship**: Enforce via `uv run ruff check`, `uv run ruff format`, `uv run black --check`; type hints validated with `uv run mypy src`.
- **Principle VII — Kid-Friendly Clarity**: Naming uses plain words (e.g., `player_helper`, `friendly_logger`); each logic block carries a one-sentence kid-friendly comment; README includes storytelling quickstart.

## Project Structure

### Documentation (this feature)

```
specs/[###-feature]/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)
<!--
  ACTION REQUIRED: Replace the placeholder tree below with the concrete layout
  for this feature. Delete unused options and expand the chosen structure with
  real paths (e.g., apps/admin, packages/something). The delivered plan must
  not include Option labels.
-->

```
src/pycraft/
├── app.py
├── cli/
│   └── pycraft.py
├── gameplay/
│   ├── controller.py
│   └── inventory.py
├── world/
│   ├── generator.py
│   └── block_manager.py
├── physics/
│   └── movement.py
└── ui/
    ├── hotbar.py
    └── menu.py

tests/
├── unit/
│   ├── test_world_generation.py
│   └── test_block_manager.py
├── integration/
│   └── test_cli_play.py
└── contract/
    └── test_save_load.py
```

**Structure Decision**: Single-project layout with layered subpackages under `src/pycraft/`; CLI adapters locked to `src/pycraft/cli/`; tests mirror layers by scope (unit/integration/contract).

## Complexity Tracking

*Fill ONLY if Constitution Check has violations that must be justified*

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
