# Data Model: Ursina Minecraft Clone

## Block
- **Purpose**: Represents a single cube in the world.
- **Fields**:
  - `id: str` — Unique identifier (e.g., `"grass"`, `"stone"`).
  - `position: tuple[int, int, int]` — World-space coordinates.
  - `texture: str` — Path/key to the texture resource.
  - `is_solid: bool` — Whether the block should block player movement.
- **Validations**:
  - `id` MUST exist in the registered block catalog.
  - `position` MUST stay within loaded chunk bounds (clamped per chunk).
- **Relationships**: Belongs to a `WorldChunk`.
- **State transitions**:
  - `Placed` → `Active` when added to chunk mesh.
  - `Active` → `Removed` when destroyed; removal triggers mesh rebuild.

## WorldChunk
- **Purpose**: Groups blocks into manageable sections for rendering and persistence.
- **Fields**:
  - `chunk_coords: tuple[int, int]` — Chunk grid position (x, z).
  - `blocks: dict[tuple[int, int, int], Block]` — Blocks keyed by local coords.
  - `mesh: Optional[Mesh]` — Cached Ursina mesh reference.
  - `needs_rebuild: bool` — Flag when block changes require mesh update.
- **Validations**:
  - `blocks` keys MUST stay within 16×32×16 local dimensions.
  - `mesh` MUST be regenerated when `needs_rebuild` becomes `True`.
- **Relationships**: Aggregated by `WorldState`; references `Block` entries.
- **State transitions**:
  - `Dirty` → `Clean` after mesh rebuild.
  - `Loaded` → `Unloaded` when chunk falls outside active radius.

## WorldState
- **Purpose**: Represents the overall world configuration in memory.
- **Fields**:
  - `seed: int` — Deterministic seed for generation.
  - `chunks: dict[tuple[int, int], WorldChunk]` — All loaded chunks.
  - `time_of_day: float` — Value between 0 and 24.
  - `active_slot: str` — Save slot currently loaded.
- **Validations**:
  - `seed` MUST be stored in save data.
  - `active_slot` MUST match an existing slot when saving/loading.
- **Relationships**: Owns `WorldChunk`; referenced by `GameSession`.
- **State transitions**:
  - `Generated` → `Active` after initial terrain build.
  - `Active` → `Persisted` after successful save.

## PlayerState
- **Purpose**: Tracks the player avatar’s state.
- **Fields**:
  - `position: Vec3` — Current world coordinates.
  - `velocity: Vec3` — Movement velocity.
  - `selected_block: str` — Block id from hotbar.
  - `inventory: dict[str, int]` — Counts of blocks per type.
  - `is_grounded: bool` — Whether the player is on a block surface.
- **Validations**:
  - `selected_block` MUST exist in the inventory.
  - `position` MUST remain within world bounds (prevent void falls below y=-64).
- **Relationships**: Contained within `GameSession`.
- **State transitions**:
  - `Idle` ↔ `Walking` depending on WASD input.
  - `Walking` → `Jumping` when space pressed and `is_grounded` true.

## GameSession
- **Purpose**: Coordinates gameplay between UI, world, and physics layers.
- **Fields**:
  - `world: WorldState` — The current world’s data.
  - `player: PlayerState` — Active player state.
  - `mode: Literal["survival", "creative"]` — Mode toggle.
  - `is_running: bool` — Loop control flag.
- **Validations**:
  - `mode` MUST match allowed values.
  - `world` and `player` MUST be initialized before loop start.
- **Relationships**: Bridges UI interactions with gameplay input handlers.
- **State transitions**:
  - `NotStarted` → `Running` when CLI launches game.
  - `Running` → `Paused` when menu opens.
  - `Running` → `Saving` → `Running` for persistence operations.

## SaveSlot
- **Purpose**: Persists world snapshots to disk.
- **Fields**:
  - `slot_id: str` — Name such as `"latest"` or `"slot1"`.
  - `path: Path` — Absolute file path under `slots/`.
  - `last_saved_at: datetime` — Timestamp of last successful save.
  - `metadata: dict[str, Any]` — Additional info (player position, mode).
- **Validations**:
  - `slot_id` MUST match allowed pattern `[a-z0-9_-]+`.
  - `path` MUST reside under repository `slots/` directory.
- **Relationships**: Connected to `WorldState` snapshots.
- **State transitions**:
  - `Empty` → `Occupied` after first save.
  - `Occupied` → `Stale` when newer unsaved changes exist.

## Hotbar
- **Purpose**: Stores quick access block types for UI.
- **Fields**:
  - `slots: list[str]` — Ordered block ids.
  - `selected_index: int` — Current hotbar position (0-based).
- **Validations**:
  - `selected_index` MUST be within `slots` length.
  - `slots` MUST contain at least one block id.
- **Relationships**: Interacts with `PlayerState` inventory updates.
- **State transitions**:
  - `Ready` → `Updated` when scroll input changes selection.
