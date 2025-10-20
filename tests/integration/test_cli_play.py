"""
Integration tests for the `pycraft play` CLI command.

We patch the heavy engine pieces so tests stay speedy.
"""

from __future__ import annotations

import json
import sys
from io import StringIO
from unittest import mock

import pytest

from pycraft.cli import pycraft as cli


def test_play_command_json_contract(monkeypatch: pytest.MonkeyPatch) -> None:
    """CLI should print JSON payload when --json is present."""

    fake_result = {"status": "starting", "scene": "overworld", "exit_code": 0}
    fake_stdout = StringIO()
    monkeypatch.setattr(sys, "stdout", fake_stdout)

    with mock.patch(
        "pycraft.cli.pycraft.run_game", return_value=fake_result
    ) as mock_run:
        exit_code = cli.main(["--json", "play", "--mode", "survival"])

    printed = json.loads(fake_stdout.getvalue())

    mock_run.assert_called_once_with(
        mode="survival", load_slot=None, verbose=False, headless=False
    )
    assert printed == {"status": "starting", "scene": "overworld"}
    assert exit_code == 0
