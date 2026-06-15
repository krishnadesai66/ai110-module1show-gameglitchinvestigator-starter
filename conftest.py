# Present so pytest adds the project root to sys.path, making top-level
# modules like logic_utils importable from tests/ regardless of how pytest
# is invoked (bare `pytest` vs `python -m pytest`).
