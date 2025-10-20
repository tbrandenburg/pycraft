"""
CLI entrypoint for Pycraft.

This module stays super tiny so it merely parses the CLI flags,
then hands everything to the library layers living under src/pycraft/.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from typing import Any

from pycraft.app import run_game, run_management_action


@dataclass
class CLIOptions:
    """Simple container so the arguments are easy to read for young learners."""

    command: str
    mode: str = "survival"
    load_slot: str | None = None
    action: str | None = None
    verbose: bool = False
    output_json: bool = False
    no_window: bool = False


def build_parser() -> argparse.ArgumentParser:
    """Create the top-level parser with two friendly subcommands."""

    parser = argparse.ArgumentParser(
        prog="pycraft",
        description="Play in a friendly block world or manage save slots.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print results as machine-readable JSON (helpful for scripts).",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    play_parser = subparsers.add_parser(
        "play", help="Launch the block world adventure."
    )
    play_parser.add_argument(
        "--mode",
        choices=("survival", "creative"),
        default="survival",
        help="Choose survival for exploring or creative for building.",
    )
    play_parser.add_argument(
        "--load",
        metavar="SLOT",
        help="Load a saved world (like 'latest' or 'slot1').",
    )
    play_parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show extra log messages for curious debuggers.",
    )
    play_parser.add_argument(
        "--no-window",
        action="store_true",
        help="Do not open a game window (useful for automated checks).",
    )

    manage_parser = subparsers.add_parser(
        "manage", help="Save or load worlds without starting the game."
    )
    manage_parser.add_argument(
        "--action",
        choices=("save", "load", "list"),
        required=True,
        help="Pick what to do with the save slots.",
    )
    manage_parser.add_argument(
        "--slot",
        help="Which slot to save to or load from (for example 'latest').",
    )
    manage_parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show extra log messages for curious debuggers.",
    )

    return parser


def parse_args(argv: list[str] | None = None) -> CLIOptions:
    """Turn CLI strings into a friendly CLIOptions dataclass."""
    parser = build_parser()
    args = parser.parse_args(argv)
    return CLIOptions(
        command=args.command,
        mode=getattr(args, "mode", "survival"),
        load_slot=getattr(args, "load", None),
        action=getattr(args, "action", None),
        verbose=getattr(args, "verbose", False),
        output_json=args.json,
        no_window=getattr(args, "no_window", False),
    )


def _print_output(payload: dict[str, Any], as_json: bool) -> None:
    """Handle both text and JSON output in a single helper."""
    if as_json:
        json_payload = dict(payload)
        json_payload.pop("exit_code", None)
        print(json.dumps(json_payload), file=sys.stdout)
        return
    message = payload.get("message", "")
    if message:
        print(message, file=sys.stdout)


def main(argv: list[str] | None = None) -> int:
    """Entry function used by `uv run pycraft ...` commands."""
    options = parse_args(argv)
    if options.command == "play":
        result = run_game(
            mode=options.mode,
            load_slot=options.load_slot,
            verbose=options.verbose,
            headless=options.no_window,
        )
    else:
        result = run_management_action(
            action=options.action or "list",
            slot=options.load_slot,
            verbose=options.verbose,
        )

    _print_output(result, options.output_json)
    return int(result.get("exit_code", 0))


if __name__ == "__main__":
    sys.exit(main())
