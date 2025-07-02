import json

from pathlib import Path

from .core import Database


DEFAULT_DB_PATH = Path.home() / "tasks.json"


def load_database(path: Path = DEFAULT_DB_PATH) -> Database:
    if not path.exists():
        return {}
    
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_database(database: Database, path: Path = DEFAULT_DB_PATH) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(database, f, indent=2)
