# Architecture

`run_task.py` copies an immutable fixture into a disposable workspace. Local tools operate only inside that workspace and reject path traversal. The verifier compares a narrow, deterministic observable (`solution.txt`) with the task definition, making the pass/fail result reproducible.

Golden solutions document the expected change without being used for scoring. A future RL adapter can reset the same fixture, expose `LocalTools` as MCP tools, and use the verifier score as a reward signal.
