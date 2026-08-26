from __future__ import annotations

import json
from pathlib import Path

from .models import Task


def repository_root() -> Path:
    return Path(__file__).resolve().parents[2]


def load_task(task_id: str) -> Task:
    path = repository_root() / "tasks" / f"{task_id}.json"
    if not path.is_file():
        raise ValueError(f"unknown task: {task_id}")
    raw = json.loads(path.read_text(encoding="utf-8"))
    return Task(
        task_id=raw["task_id"],
        category=raw["category"],
        language=raw["language"],
        description=raw["description"],
        required_tools=tuple(raw["required_tools"]),
        timeout_seconds=raw["timeout_seconds"],
        expected_output=raw["expected_output"],
    )


def list_tasks() -> list[Task]:
    return [load_task(path.stem) for path in sorted((repository_root() / "tasks").glob("*.json"))]
