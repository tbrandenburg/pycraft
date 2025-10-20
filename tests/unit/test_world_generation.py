"""
Unit tests for the flat world generator.

These tests describe what a friendly block world should look like.
"""

from __future__ import annotations

import pytest

from pycraft.world.generator import build_flat_world


def test_flat_world_height() -> None:
    """Flat world should create a two-layer terrain with air above."""

    world = build_flat_world(width=4, depth=4, height=8)

    assert len(world) == 4 * 4 * 2, "World must contain ground and surface blocks."

    ground_blocks = {pos for pos, block_id in world.items() if block_id == "grass"}
    dirt_blocks = {pos for pos, block_id in world.items() if block_id == "dirt"}

    assert all(y == 0 for (_, y, _) in ground_blocks), "Grass sits at y=0."
    assert all(y == -1 for (_, y, _) in dirt_blocks), "Dirt sits just below grass."


def test_flat_world_invalid_dimensions() -> None:
    """Generator protects against tiny worlds."""

    with pytest.raises(ValueError):
        build_flat_world(width=0, depth=4, height=4)
