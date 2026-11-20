"""Safe printing helpers.

`print()` inside Flet event handlers can raise BrokenPipeError when the
process stdout is piped and the reader closes (e.g. `flet run --web | head`,
or when the terminal is closed). This module provides a drop-in replacement
that swallows those errors so handlers never crash.
"""

import sys


def safe_print(*args, **kwargs) -> None:
    """Print like the built-in but ignore BrokenPipeError / closed stdout."""
    try:
        print(*args, **kwargs)
    except (BrokenPipeError, OSError, ValueError):
        pass


def silence_stdout() -> None:
    """Redirect stdout/stderr to a no-op stream (useful for web servers)."""
    try:
        sys.stdout.close()
    except Exception:
        pass
