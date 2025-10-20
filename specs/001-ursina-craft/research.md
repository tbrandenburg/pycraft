# Research: Ursina Minecraft Clone

## Physics helper selection
- **Decision**: Use Ursina’s built-in `Entity` collision and `BoxCollider` components with a thin wrapper module in `src/pycraft/physics/movement.py`.
- **Rationale**: Ursina already integrates Bullet physics-lite primitives that match our block world needs; wrapping them keeps the kid-friendly API while avoiding extra dependencies.
- **Alternatives considered**:
  - Panda3D physics: heavier integration and duplicates Ursina’s abstractions.
  - PyBullet: high-fidelity but overkill for axis-aligned block interactions.

## Static typing workflow
- **Decision**: Add `mypy` as the static type checker and run it via `uv run mypy src`.
- **Rationale**: `mypy` aligns with Python 3.12 typing, integrates with uv easily, and complements ruff/black for Constitution Principle VI.
- **Alternatives considered**:
  - Pyright: excellent but requires Node/npm tooling, increasing setup complexity.
  - Ruff type checker (experimental): still maturing and lacks rich type coverage for Ursina stubs.

## Ursina architecture patterns
- **Decision**: Structure gameplay around Ursina `Entity` subclasses grouped by layer modules (UI/gameplay/world) and keep engine initialization inside `run_game`.
- **Rationale**: Following Ursina’s recommended entity hierarchy simplifies rendering, and isolating engine start keeps CLI orchestration thin.
- **Alternatives considered**:
  - Procedural scene creation without subclasses: harder to maintain and comment for young learners.
  - Third-party scene graph managers: unnecessary for core feature scope.

## UV project workflows
- **Decision**: Initialize with `uv init`, manage dependencies via `uv add`, run tools through `uv run`, and export lockfile with `uv export --locked > uv.lock`.
- **Rationale**: Matches Constitution guardrail and keeps reproducible environments for testers.
- **Alternatives considered**:
  - Poetry: strong but deviates from Constitution mandate.
  - pip-tools: lacks built-in task execution flow required for CLI commands.

## Formatting and linting
- **Decision**: Use `ruff` for lint + format (`uv run ruff check`, `uv run ruff format`) and keep `black` as backup formatter invoked with `uv run black`.
- **Rationale**: Ruff provides fast PEP 8 enforcement with fine-grained rules; black ensures consistent formatting for contributors familiar with it.
- **Alternatives considered**:
  - Only black + isort: slower feedback, fewer lint rules.
  - autopep8: less opinionated and misses structural linting.

## Pytest coverage plan
- **Decision**: Organize pytest suites into unit (block/world logic), integration (CLI + engine bootstrap via Ursina test harness), and contract (save/load JSON).
- **Rationale**: Mirrors Constitution Principle III and keeps test intent clear for young learners.
- **Alternatives considered**:
  - Nose/unittest: less modern and verbose.
  - Single test directory: harder to spotlight failing layer during reviews.

## World persistence format
- **Decision**: Store worlds as compressed JSON (`.world` = gzipped JSON) describing block arrays and metadata.
- **Rationale**: Human-readable structure aids teaching moments, compression keeps files small (~100 KB per 16×16×32 chunk).
- **Alternatives considered**:
  - Binary pickle: compact but opaque and security-sensitive.
  - SQLite: durable but adds dependency and complexity beyond scope.
