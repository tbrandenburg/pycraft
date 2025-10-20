"""
World generation helpers for Pycraft.

These functions produce a super simple flat world so young builders
can start placing blocks right away.
"""

from __future__ import annotations

BlockPosition = tuple[int, int, int]


def build_flat_world(
    width: int = 16, depth: int = 16, height: int = 32
) -> dict[BlockPosition, str]:
    """
    Build a flat world represented as a dictionary of block positions to block ids.

    The ground is a cozy dirt layer with a grass carpet on top so players
    can explore without falling. Height controls how much empty space sits above.
    """

    if width <= 0 or depth <= 0 or height <= 0:
        raise ValueError("World dimensions must be positive numbers.")

    blocks: dict[BlockPosition, str] = {}

    for x in range(width):
        for z in range(depth):
            # Lay down dirt just below the surface.
            blocks[(x, -1, z)] = "dirt"
            # Cover the dirt with soft grass.
            blocks[(x, 0, z)] = "grass"

    return blocks
