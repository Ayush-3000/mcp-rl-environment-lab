from __future__ import annotations

import shutil
from pathlib import Path

from .catalog import load_task, repository_root
from .models import VerificationResult


def prepare_workspace(task_id: str, destination: Path) -> Path:
    source = repository_root() / "fixtures" / task_id
    if not source.is_dir():
        raise ValueError(f"fixture missing for {task_id}")
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(source, destination)
    return destination


def verify(task_id: str, workspace: Path) -> VerificationResult:
    task = load_task(task_id)
    output = (workspace / "solution.txt")
    actual = output.read_text(encoding="utf-8").strip() if output.exists() else ""
    passed = actual == task.expected_output
    return VerificationResult(
        task_id=task_id,
        passed=passed,
        reason="expected deterministic output produced" if passed else "solution.txt does not match expected output",
        score=100 if passed else 0,
        workspace=workspace,
    )
