import pytest

from src.core import add_task, update_task


@pytest.fixture
def empty_db():
    return {}


def test_add_task(empty_db):
    result = add_task(empty_db, "Study pytest")
    assert "1" in result
    assert result["1"]["description"] == "Study pytest"
    assert result["1"]["status"] == "todo"
    assert len(empty_db) == 1


def test_update_task(empty_db):
    add_task(empty_db, "Study English")
    updated = update_task(empty_db, "1", "Study Python")
    assert updated["1"]["description"] == "Study Python"
    assert "updated-at" in updated["1"]
