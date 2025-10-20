# Feature Specification: Ursina Minecraft Clone

**Feature Branch**: `feature/001-ursina-craft`  
**Created**: 2025-10-20  
**Status**: Draft  
**Input**: User description: "/speckit.specify Build a python based simple minecraft clone. It should be based on ursina. It should be a uv managed project. Use black for formatting and PEP8 naming conventions. Write the code so that a 12 year old child understands it, with less complex code and more descriptive and easy-to-understand comments. Apply a layered architecture for separating UI from gaming, world and physic logic. Apply basic pytest testing. I am using git flow as my branching strategy and state-of-the-art commit conventions. I don't have special domain specific constraints."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Explore a Friendly Block World (Priority: P1)

As a curious player, I want to walk around a bright block world so that I can explore and see the land from first person view.

**Why this priority**: Movement and camera control are the foundation for every other gameplay loop.

**Independent Test**: Launch the CLI play command, confirm a player can move with WASD and jump with space while the camera follows smoothly.

**CLI Contract**: Command `uv run pycraft play` → stdout ("Launching Ursina sandbox...") | `--json` (`{"status": "starting", "scene": "overworld"}`) | stderr on failure ("Could not start Ursina engine") | exit codes `[0 success, 11 engine_init_error, 12 config_missing]`

**Library Touchpoints**: `src/pycraft/app.py`: `run_game()` sets up layers; `src/pycraft/world/generator.py`: `build_flat_world()` prepares initial terrain.

**Kid-Friendly Explanation**: "When I press play, we build a toy world full of cubes and let my player run around like an excited explorer."

**Acceptance Scenarios**:

1. **Given** the project dependencies are installed, **When** I run `uv run pycraft play`, **Then** a window opens showing a block world and the console prints "Launching Ursina sandbox...".
2. **Given** the game window is active, **When** I press `W`, **Then** the player moves forward and the camera follows without jitter.

---

### User Story 2 - Build and Break Blocks (Priority: P2)

As a maker, I want to add or remove blocks on the ground so that I can shape the world into whatever I imagine.

**Why this priority**: Building and breaking blocks create the creative loop that makes the clone fun.

**Independent Test**: Start the world, point at a block, click left to remove it, click right to place a new block, and verify the world data updates instantly.

**CLI Contract**: Command `uv run pycraft play --mode creative` | stdout ("Creative tools ready") | `--json` (`{"status": "starting", "mode": "creative"}`) | stderr on failure ("Creative mode toggle failed") | exit codes `[0 success, 21 creative_toggle_error]`

**Library Touchpoints**: `src/pycraft/world/block_manager.py`: `add_block()` and `remove_block()`; `src/pycraft/ui/hotbar.py`: `select_block_type()`.

**Kid-Friendly Explanation**: "I can poke a block to make it pop away or place a new block like building with digital Lego bricks."

**Acceptance Scenarios**:

1. **Given** I start the game in creative mode, **When** I right-click a block, **Then** a new block of the selected type appears.
2. **Given** a block is placed, **When** I left-click it, **Then** the block disappears and the hotbar count updates.

---

### User Story 3 - Save and Reload My Build (Priority: P3)

As a returning player, I want to save my changed world and load it later so that my creations stay safe.

**Why this priority**: Persistence keeps players engaged between sessions.

**Independent Test**: After modifying blocks, run the save command, close the game, restart it with `--load latest`, and confirm the changes reappear.

**CLI Contract**: Command `uv run pycraft manage --action save --slot latest` | stdout ("World saved to slots/latest.world") | `--json` (`{"status": "saved", "slot": "latest"}`) | stderr on failure ("Save failed: [reason]") | exit codes `[0 success, 31 save_error, 32 load_error]`

**Library Touchpoints**: `src/pycraft/persistence/storage.py`: `save_world()` and `load_world()`; `src/pycraft/ui/menu.py`: `show_save_confirmation()`.

**Kid-Friendly Explanation**: "When I press save, we bottle up my block castle so I can open the same jar next time."

**Acceptance Scenarios**:

1. **Given** I changed blocks, **When** I run the save command, **Then** a `slots/latest.world` file is created and the console says "World saved".
2. **Given** a saved world exists, **When** I start the game with `--load latest`, **Then** the saved layout appears exactly as before.

---

[Add more user stories as needed, each with an assigned priority]

### Edge Cases

- What happens when the Ursina engine cannot access GPU resources? (Include exit code `11` and stderr suggesting to update video drivers)
- How does system handle loading a missing save slot? (Describe logs surfaced with `--verbose` that clarify the file path and suggest creating a new world)

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Library module at `src/pycraft/app.py` MUST expose `run_game(mode: str = "survival")` with documented inputs/outputs.
- **FR-002**: CLI command `pycraft play` MUST invoke the library module and respect the documented stdout/stderr contract.
- **FR-003**: Tests in `tests/unit/test_world_generation.py` MUST fail before implementation and pass afterward.
- **FR-004**: Integration/contract test in `tests/integration/test_cli_play.py` MUST cover user story acceptance.
- **FR-005**: Logging MUST emit structured key/value details and support `--verbose` toggling.
- **FR-006**: Repository MUST be managed with `uv` (`uv init`, `uv add`, `uv run`, `uv export --locked`) and document the commands in docs.
- **FR-007**: Source code MUST pass `uv run ruff check`, `uv run ruff format --check`, and include friendly comments that explain logic in plain language.
- **FR-008**: Layered architecture MUST separate UI (`src/pycraft/ui/`), gameplay (`src/pycraft/gameplay/`), world (`src/pycraft/world/`), and physics (`src/pycraft/physics/`) modules with clear interfaces.
- **FR-009**: Pytest suites MUST cover player movement, block placement/removal, and persistence serialization.

*Example of marking unclear requirements:*

- **FR-010**: System MUST authenticate users via [NEEDS CLARIFICATION: auth method not specified - email/password, SSO, OAuth?]
- **FR-011**: System MUST retain user data for [NEEDS CLARIFICATION: retention period not specified]

### Key Entities *(include if feature involves data)*

- **Block**: Represents a cube with type (grass, dirt, stone), position (x, y, z), and texture reference.
- **WorldChunk**: Contains a collection of Blocks, chunk coordinates, and mesh data for rendering.
- **PlayerState**: Tracks position, velocity, currently selected block type, and inventory counts.
- **SaveSlot**: Stores metadata about saved games, including timestamp, slot name, and file path.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Player can walk around 16×16×32 block world at 30 FPS on mid-range hardware.
- **SC-002**: `uv run pytest` completes under 60 seconds with all tests passing.
- **SC-003**: `uv run ruff check` and `uv run ruff format --check` report zero findings on main branch.
- **SC-004**: `uv run pycraft play --json` returns structured output matching the documented schema.
- **SC-005**: A 12-year-old user can read the README quickstart and explain how to run, build, and save the world.
