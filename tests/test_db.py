import json

from pathlib import Path

from src.db import load_database, save_database
from src.core import create_task


def test_save_and_load_database(tmp_path: Path):
    db_path = tmp_path / "test_tasks.json"
    sample_data = {
        "1": create_task("Test persistence")
    }

    save_database(sample_data, path=db_path)

    assert db_path.exists()
    content = json.loads(db_path.read_text())
    assert content["1"]["description"] == "Test persistence"
    assert content["1"]["status"] == "todo"

    loaded = load_database(path=db_path)
    assert loaded == sample_data


def test_load_nonexistent_file(tmp_path: Path):
    fake_path = tmp_path / "does_not_exist.json"
    loaded = load_database(path=fake_path)
    assert loaded == {}
