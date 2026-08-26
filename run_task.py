from __future__ import annotations

import argparse
from pathlib import Path

from mcp_rl_lab.catalog import list_tasks
from mcp_rl_lab.runner import prepare_workspace, verify


def main() -> int:
    parser = argparse.ArgumentParser(description="Prepare or verify a deterministic coding task.")
    parser.add_argument("task_id", nargs="?", help="for example task_001")
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--workspace", type=Path, default=Path(".task-workspace"))
    parser.add_argument("--list", action="store_true")
    args = parser.parse_args()
    if args.list:
        for task in list_tasks():
            print(f"{task.task_id}: {task.language} {task.category}")
        return 0
    if not args.task_id:
        parser.error("task_id is required unless --list is used")
    if args.verify:
        result = verify(args.task_id, args.workspace)
        print(f"{result.task_id}: {'PASS' if result.passed else 'FAIL'} ({result.reason})")
        return 0 if result.passed else 1
    workspace = prepare_workspace(args.task_id, args.workspace)
    print(f"prepared {args.task_id} in {workspace}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
