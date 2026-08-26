from pathlib import Path

import pytest

from mcp_rl_lab.catalog import list_tasks, load_task
from mcp_rl_lab.runner import prepare_workspace, verify


def test_catalog_has_balanced_tasks() -> None:
    tasks = list_tasks()
    assert len(tasks) == 8
    assert {task.category for task in tasks} == {"bug-fixing", "feature", "refactoring", "performance"}
    assert {task.language for task in tasks} == {"python", "typescript"}


def test_prepare_and_verify(task_tmp: Path = Path(".pytest-task")) -> None:
    workspace = prepare_workspace("task_001", task_tmp)
    assert verify("task_001", workspace).passed


def test_wrong_solution_fails(tmp_path: Path) -> None:
    workspace = prepare_workspace("task_002", tmp_path / "task")
    (workspace / "solution.txt").write_text("wrong", encoding="utf-8")
    assert not verify("task_002", workspace).passed


def test_unknown_task_is_rejected() -> None:
    with pytest.raises(ValueError, match="unknown task"):
        load_task("missing")
