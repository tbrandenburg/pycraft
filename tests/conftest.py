"""
Shared pytest fixtures for the Pycraft project.

These fixtures keep tests tidy and easy to understand for young readers.
"""

from __future__ import annotations

import json
import sys
from collections.abc import Iterator
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))


@pytest.fixture()
def temp_slots(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Iterator[Path]:
    """
    Provide an isolated slots directory for save/load tests.

    Each test gets its own folder so saves never bump into each other.
    """

    slots_dir = tmp_path / "slots"
    slots_dir.mkdir()
    monkeypatch.setenv("PYCRAFT_SLOTS_PATH", str(slots_dir))
    yield slots_dir


@pytest.fixture()
def json_printer() -> dict[str, str]:
    """
    Collect JSON output to make CLI tests easy.

    Instead of reading stdout directly, tests can inspect this dictionary.
    """

    return {"last": json.dumps({"status": "starting"})}
