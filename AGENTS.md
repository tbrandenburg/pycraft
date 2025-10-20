# pycraft Development Guidelines

Auto-generated from all feature plans. Last updated: 2025-10-20

## Active Technologies
- Python 3.12 + Ursina engine, uv package manager, ruff, black, pytest, mypy (001-ursina-craft)

## Project Structure
```
src/
tests/
```

## Commands
```bash
uv run pycraft play --mode survival --json
uv run pycraft manage --action save --slot latest
uv run pytest
uv run ruff check
uv run ruff format --check
uv run black --check src tests
uv run mypy src
```

## Code Style
Python 3.12: Follow standard conventions

## Recent Changes
- 001-ursina-craft: Added Python 3.12 + Ursina engine, uv package manager, ruff, black, pytest, mypy

<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->
