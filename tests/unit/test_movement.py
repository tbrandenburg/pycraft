"""
Unit tests for movement helpers.

These tests keep the math simple and friendly.
"""

from __future__ import annotations

import math

import pytest

from pycraft.physics.movement import calculate_step


def test_wasd_moves_player() -> None:
    """Diagonal input should normalize so the player speed feels stable."""

    step_x, step_z = calculate_step((1.0, 1.0), speed=5.0)
    assert math.isclose(step_x, step_z, rel_tol=1e-5)
    assert math.isclose(math.hypot(step_x, step_z), 5.0, rel_tol=1e-5)


def test_invalid_input_raises() -> None:
    """Reject tuples that are not two numbers."""

    with pytest.raises(ValueError):
        calculate_step((1.0,), speed=5.0)  # type: ignore[arg-type]
