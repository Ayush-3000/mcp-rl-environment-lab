from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Task:
    task_id: str
    category: str
    language: str
    description: str
    required_tools: tuple[str, ...]
    timeout_seconds: int
    expected_output: str


@dataclass(frozen=True)
class VerificationResult:
    task_id: str
    passed: bool
    reason: str
    score: int
    workspace: Path
