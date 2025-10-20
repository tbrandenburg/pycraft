# Quickstart: Ursina Minecraft Clone

## 1. Prepare tools
1. Install Python 3.12 (use pyenv if needed).
2. Install `uv`: `pip install uv` (or use the official installer).
3. Clone the repository and checkout branch `001-ursina-craft`.

## 2. Set up the project
```bash
uv init --package pycraft
uv add ursina pytest ruff black mypy
uv run python -m pip install -e .
uv export --locked > uv.lock
```

## 3. Run the friendly sandbox
```bash
uv run pycraft play --mode survival --json
```
- Expect stdout: `{"status": "starting", "scene": "overworld"}`
- Use `--verbose` to see extra log hints if something breaks.

## 4. Save your world
```bash
uv run pycraft manage --action save --slot latest
uv run pycraft play --load latest
```
- Save slots live under `slots/`.
- The CLI prints stories so younger players know what just happened.

## 5. Run tests and quality checks
```bash
uv run pytest
uv run ruff check
uv run ruff format --check
uv run black --check src tests
uv run mypy src
```

## 6. Coding style
- Keep modules inside `src/pycraft/` and use layered folders: `ui`, `gameplay`, `world`, `physics`.
- Add short, cheerful comments above each logic block so a 12-year-old can follow the story.
- Follow git-flow: create feature branches like `001-ursina-craft` and use conventional commits.

## 7. Troubleshooting
- Ursina window blank? Run with `--verbose` and check GPU drivers.
- Save load fails? Confirm `slots/latest.world` exists and isn’t empty.
- Tooling missing? Re-run `uv sync` to install dependencies.
