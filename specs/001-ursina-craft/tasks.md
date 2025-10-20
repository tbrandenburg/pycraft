---
description: "Task list for Ursina Minecraft Clone feature implementation"
---

# Tasks: Ursina Minecraft Clone

**Input**: Design documents from `/specs/001-ursina-craft/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are REQUIRED per Constitution Principle III. List the failing test tasks before implementation tasks and mark when they will be executed. Include PEP 8 tooling (`uv run ruff check`, `uv run ruff format`) alongside unit/integration suites.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`
- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions
- **Single project**: `src/`, `tests/` at repository root
- Paths shown below follow the layered structure in plan.md

<!--
  ============================================================================
  IMPORTANT: Tasks below are concrete deliverables for this feature.
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Configure uv-managed project metadata (Python 3.12, package name, scripts) in pyproject.toml
- [ ] T002 Declare runtime and tooling dependencies with `uv add` (ursina, pytest, ruff, black, mypy) in pyproject.toml
- [ ] T003 Export locked dependency snapshot with `uv export --locked > uv.lock`
- [ ] T004 Add kid-friendly contribution guidelines section to README.md explaining storytelling comments

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T005 Scaffold layered package skeleton (src/pycraft/__init__.py and subpackages cli, gameplay, world, physics, persistence, ui)
- [ ] T006 Create CLI bootstrap module with entrypoint stub in src/pycraft/cli/pycraft.py
- [ ] T007 Establish configuration for styling tools in ruff.toml
- [ ] T008 Configure static typing rules for mypy in mypy.ini
- [ ] T009 Configure pytest defaults and test discovery markers in pytest.ini
- [ ] T010 Initialize test package layout with __init__.py and conftest helpers in tests/conftest.py
- [ ] T011 Document save-slot storage expectations for young players in slots/README.md

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Explore a Friendly Block World (Priority: P1) 🎯 MVP

**Goal**: Let players launch the sandbox, walk around a bright block world, and keep camera movement smooth.

**Independent Test**: Run `uv run pycraft play --json`; verify window opens, player moves with WASD + jump, camera follows, JSON output matches schema.

### Tests for User Story 1 (Required) ⚠️

**NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T012 [P] [US1] Author flat-world generation unit test in tests/unit/test_world_generation.py::test_flat_world_height
- [ ] T013 [P] [US1] Add player movement physics unit test in tests/unit/test_movement.py::test_wasd_moves_player
- [ ] T014 [P] [US1] Add CLI play JSON integration test in tests/integration/test_cli_play.py::test_play_command_json_contract

### Implementation for User Story 1

- [ ] T015 [P] [US1] Implement flat terrain builder in src/pycraft/world/generator.py
- [ ] T016 [P] [US1] Implement movement helpers with Ursina colliders in src/pycraft/physics/movement.py
- [ ] T017 [US1] Implement gameplay controller handling input + camera follow in src/pycraft/gameplay/controller.py
- [ ] T018 [US1] Orchestrate Ursina engine startup and layer wiring in src/pycraft/app.py
- [ ] T019 [US1] Wire CLI play command with `--json` and `--verbose` flags in src/pycraft/cli/pycraft.py
- [ ] T020 [US1] Add cheerful, kid-friendly comments explaining exploration flow in src/pycraft/app.py and src/pycraft/gameplay/controller.py
- [ ] T021 [US1] Run `uv run pytest -k "(world_generation or movement)"` to confirm US1 tests pass
- [ ] T022 [US1] Run `uv run ruff check` and `uv run ruff format` on src/pycraft/world/ src/pycraft/gameplay/ src/pycraft/physics/ to ensure PEP 8 compliance

**Checkpoint**: At this point, User Story 1 should be fully functional, test suite green, and CLI contract verified

---

## Phase 4: User Story 2 - Build and Break Blocks (Priority: P2)

**Goal**: Allow creative players to place and destroy blocks with a friendly hotbar interface.

**Independent Test**: Start creative mode with `uv run pycraft play --mode creative --json`; place and remove blocks while verifying hotbar updates and JSON reflects mode.

### Tests for User Story 2 (Required) ⚠️

- [ ] T023 [P] [US2] Add block manager unit tests covering add/remove behavior in tests/unit/test_block_manager.py
- [ ] T024 [P] [US2] Extend CLI play integration test for creative mode toggle in tests/integration/test_cli_play.py::test_creative_mode_contract
- [ ] T025 [P] [US2] Add UI hotbar snapshot test ensuring selection updates in tests/integration/test_cli_ui.py::test_hotbar_selection_cycles

### Implementation for User Story 2

- [ ] T026 [P] [US2] Implement block manager with chunk updates in src/pycraft/world/block_manager.py
- [ ] T027 [P] [US2] Build hotbar UI with selection logic in src/pycraft/ui/hotbar.py
- [ ] T028 [US2] Extend gameplay controller for build/destroy modes in src/pycraft/gameplay/controller.py
- [ ] T029 [US2] Update CLI and game session to honor `--mode creative` in src/pycraft/cli/pycraft.py
- [ ] T030 [US2] Refresh comments so block-building logic reads like digital Lego instructions in src/pycraft/world/block_manager.py and src/pycraft/ui/hotbar.py
- [ ] T031 [US2] Run `uv run pytest -k "(block_manager or creative)"` to confirm US2 tests pass
- [ ] T032 [US2] Run `uv run ruff check` and `uv run ruff format` on src/pycraft/world/ src/pycraft/ui/ to ensure style stays clean

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently with passing tests and CLI verification

---

## Phase 5: User Story 3 - Save and Reload My Build (Priority: P3)

**Goal**: Persist world changes to save slots and reload them through the CLI with narrative feedback.

**Independent Test**: Modify blocks, run `uv run pycraft manage --action save --slot latest`, close the app, restart with `uv run pycraft play --load latest --json`, and confirm world state matches saved version.

### Tests for User Story 3 (Required) ⚠️

- [ ] T033 [P] [US3] Add save/load contract test verifying slot round-trip in tests/contract/test_save_load.py
- [ ] T034 [P] [US3] Add CLI manage integration test for save action in tests/integration/test_cli_manage.py::test_save_slot_roundtrip
- [ ] T035 [P] [US3] Add persistence unit test for world serialization/deserialization in tests/unit/test_persistence.py

### Implementation for User Story 3

- [ ] T036 [P] [US3] Implement persistence helpers for gzipped JSON worlds in src/pycraft/persistence/storage.py
- [ ] T037 [US3] Extend menu UI to display save confirmation and kid-friendly hints in src/pycraft/ui/menu.py
- [ ] T038 [US3] Extend CLI manage command to call persistence helpers and emit JSON responses in src/pycraft/cli/pycraft.py
- [ ] T039 [US3] Update quickstart to document save/load workflow in specs/001-ursina-craft/quickstart.md
- [ ] T040 [US3] Run `uv run pytest -k "(save_load or persistence)"` to confirm US3 tests pass
- [ ] T041 [US3] Run `uv run ruff check` and `uv run ruff format` on src/pycraft/persistence/ src/pycraft/ui/menu.py to keep style aligned

**Checkpoint**: All user stories should now be independently functional with no outstanding waivers

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T042 Document full storytelling quickstart and troubleshooting tips for young players in README.md
- [ ] T043 Produce sample world asset for demos in slots/sample.world and describe it in slots/README.md
- [ ] T044 Run full quality suite (`uv run pytest`, `uv run ruff check`, `uv run ruff format --check`, `uv run black --check src tests`, `uv run mypy src`) and capture results in AGENTS.md
- [ ] T045 Review performance (≥30 FPS) and jot findings in docs/performance.md
- [ ] T046 Prepare release notes and compliance checklist in docs/release-notes.md
- [ ] T047 Pair-review code comments with a young learner or mentor, documenting feedback in docs/kid-review.md

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories proceed in priority order (US1 → US2 → US3)
- **Polish (Final Phase)**: Depends on all user stories completing

### User Story Dependencies

- **User Story 1 (P1)**: First deliverable; no upstream story dependencies
- **User Story 2 (P2)**: Depends on US1 world generation and controller scaffolding
- **User Story 3 (P3)**: Depends on US1 gameplay loop and US2 block management for persistence payloads

### Within Each User Story

- Tests MUST be written and observed failing before implementation
- Implement supporting modules (world/physics/ui) before CLI orchestration
- Keep comments story-friendly and update quickstart alongside code
- Story complete before moving to next priority

### Parallel Opportunities

- Setup tasks T001–T004 can run in parallel
- Foundational tasks T005–T011 can be split across devs (different files)
- In US1, tests T012–T014 and implementations T015–T019 touching separate modules allow parallel work
- US2 hotbar/UI tasks T026–T027 can proceed alongside CLI updates T029
- US3 persistence logic T036 and menu updates T037 can progress while CLI wiring T038 is in review

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
uv run pytest tests/unit/test_world_generation.py
uv run pytest tests/unit/test_movement.py
uv run pytest tests/integration/test_cli_play.py::test_play_command_json_contract

# Launch all models for User Story 1 together:
python -m build_block_generator src/pycraft/world/generator.py  # (dev helper script, optional)
touch src/pycraft/physics/movement.py  # ensure file exists before implementation
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Deliver User Story 1 → Test independently → Demo (MVP)
3. Deliver User Story 2 → Test independently → Demo creative tools
4. Deliver User Story 3 → Test independently → Demo save/load
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group, starting with tests that prove the change
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
- Keep comments friendly: imagine explaining the code to a curious 12-year-old and capture that wording inline
