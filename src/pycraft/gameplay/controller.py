"""
Gameplay controller that glues together input, camera, and world state.

We will keep everything easy to read so younger coders can follow along.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from pycraft.physics.movement import calculate_step

DEFAULT_HEIGHT = 1.8  # average height so the viewpoint feels natural
GRAVITY = -9.81


@dataclass
class PlayerController:
    """Simple data class describing the player state."""

    speed: float = 5.0
    jump_force: float = 1.0
    is_grounded: bool = True
    position: tuple[float, float, float] = field(
        default_factory=lambda: (0.0, DEFAULT_HEIGHT, 0.0)
    )
    velocity_y: float = 0.0


def create_controller(speed: float = 5.0, jump_force: float = 6.0) -> PlayerController:
    """
    Factory helper for the controller.

    The controller starts grounded at a comfy height so younger players see the world.
    """

    return PlayerController(speed=speed, jump_force=jump_force)


def update_controller(
    controller: PlayerController,
    dt: float,
    input_vector: tuple[float, float] | None = None,
    wants_to_jump: bool = False,
) -> None:
    """
    Step the controller and move the player around.

    Parameters:
        controller: current player controller instance.
        dt: delta time between frames.
        input_vector: tuple describing horizontal input (x, z).
        wants_to_jump: whether the jump action was requested this frame.
    """

    horizontal_step = (0.0, 0.0)
    if input_vector:
        horizontal_step = calculate_step(input_vector, controller.speed)

    x, y, z = controller.position
    # Glide sideways based on the player's chosen direction.
    x += horizontal_step[0] * dt
    z += horizontal_step[1] * dt

    if wants_to_jump and controller.is_grounded:
        # A little boost helps the player hop when their feet are on the ground.
        controller.velocity_y = controller.jump_force
        controller.is_grounded = False

    controller.velocity_y += GRAVITY * dt
    y += controller.velocity_y * dt

    if y <= DEFAULT_HEIGHT:
        # Snap back to ground so the explorer never sinks below the grass.
        y = DEFAULT_HEIGHT
        controller.velocity_y = 0.0
        controller.is_grounded = True

    controller.position = (x, y, z)
