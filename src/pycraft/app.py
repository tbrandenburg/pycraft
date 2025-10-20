"""
Top-level application orchestration for Pycraft.

This module will connect the CLI to the Ursina engine. For now it provides
placeholder functions so tests can fail meaningfully during TDD.
"""

from __future__ import annotations

import logging

from pycraft.gameplay.controller import create_controller, update_controller
from pycraft.world.generator import build_flat_world

LOGGER = logging.getLogger("pycraft")


def run_game(
    mode: str = "survival",
    load_slot: str | None = None,
    verbose: bool = False,
) -> dict[str, object]:
    """
    Launch the friendly block world.

    The actual Ursina loop will be connected later. For now we simulate the world
    setup so the CLI contract has real data to share.
    """

    logging.basicConfig(level=logging.DEBUG if verbose else logging.INFO)
    LOGGER.info("Launching Ursina sandbox...")

    # Build a flat playground so the adventurer has somewhere safe to walk.
    world = build_flat_world()
    controller = create_controller()
    # Nudge the controller so we return a tidy starting position.
    update_controller(controller, dt=0.0, input_vector=None)

    payload: dict[str, object] = {
        "status": "starting",
        "scene": "overworld",
        "mode": mode,
        "load_slot": load_slot,
        "player_position": controller.position,
        "world_blocks": len(world),
        "message": "Launching Ursina sandbox...",
        "exit_code": 0,
    }

    if load_slot is None:
        payload.pop("load_slot")

    return payload


def run_management_action(
    action: str,
    slot: str | None,
    verbose: bool = False,
) -> dict[str, object]:
    """
    Handle save/load operations from the CLI.

    Stub ensures contract tests fail until persistence is implemented.
    """

    raise NotImplementedError("Management actions not yet implemented.")
