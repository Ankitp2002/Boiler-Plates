from __future__ import annotations

from pathlib import Path
import sys


def ensure_projects_on_path() -> None:
    """
    Ensure both `AgenticSuite/` and sibling projects are importable.

    - `AgenticSuite/` contains the suite skeletons.
    - `gp_system_agentic/` is a sibling project under `projects/`.
    """

    projects_root = Path(__file__).resolve().parents[2]
    agentic_suite_root = projects_root / "AgenticSuite"
    gp_system_root = projects_root / "gp_system_agentic"

    for p in (str(agentic_suite_root), str(gp_system_root)):
        if p not in sys.path:
            sys.path.insert(0, p)


ensure_projects_on_path()

