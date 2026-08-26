"""Local deterministic tools suitable for a lightweight MCP adapter."""
from __future__ import annotations

from pathlib import Path


class LocalTools:
    def __init__(self, root: Path) -> None:
        self.root = root.resolve()

    def _safe_path(self, relative_path: str) -> Path:
        candidate = (self.root / relative_path).resolve()
        if self.root not in candidate.parents and candidate != self.root:
            raise ValueError("path escapes task workspace")
        return candidate

    def list_directory(self, relative_path: str = ".") -> list[str]:
        path = self._safe_path(relative_path)
        return sorted(child.name for child in path.iterdir())

    def read_file(self, relative_path: str) -> str:
        return self._safe_path(relative_path).read_text(encoding="utf-8")

    def search_code(self, needle: str) -> list[str]:
        matches: list[str] = []
        for path in self.root.rglob("*"):
            if path.is_file() and needle in path.read_text(encoding="utf-8"):
                matches.append(path.relative_to(self.root).as_posix())
        return sorted(matches)

    def inspect_test_results(self) -> dict[str, str]:
        return {"status": "not-run", "source": "deterministic local fixture"}
