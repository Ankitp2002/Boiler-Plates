from __future__ import annotations

from pathlib import Path
import sys


def ensure_suite_on_path() -> None:
    suite_root = Path(__file__).resolve().parents[1]
    suite_root_str = str(suite_root)
    if suite_root_str not in sys.path:
        sys.path.insert(0, suite_root_str)


ensure_suite_on_path()

