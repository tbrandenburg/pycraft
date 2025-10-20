"""
Movement helpers for the friendly player avatar.

These utilities wrap Ursina so the rest of the code reads nicely.
"""

from __future__ import annotations

import math


def calculate_step(
    input_vector: tuple[float, float], speed: float = 5.0
) -> tuple[float, float]:
    """
    Turn horizontal input into a movement step.

    The function keeps diagonal motion from feeling faster by normalizing
    the input vector before scaling it by the desired speed.
    """

    if len(input_vector) != 2:
        raise ValueError("Input vector must contain two values (x and z).")

    x, z = input_vector
    if x == 0 and z == 0:
        return (0.0, 0.0)

    magnitude = math.hypot(x, z)
    normalized_x = x / magnitude
    normalized_z = z / magnitude
    return (normalized_x * speed, normalized_z * speed)
