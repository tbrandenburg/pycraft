# Slots Directory

This folder holds saved worlds for the friendly block adventure.

- Every save file ends with `.world` and stores gzipped JSON data.
- Slot names use simple words like `latest`, `slot1`, or `castle`.
- During tests we point the game to a temporary slots folder so real saves stay safe.
- Remember: never store secrets here—just block stories you want to revisit!

When running CLI commands:

```bash
uv run pycraft manage --action save --slot latest
uv run pycraft play --load latest
```

Those commands keep everything inside this directory so it is easy to share worlds.
