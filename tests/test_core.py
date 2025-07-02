import pytest

from src.core import add_task


@pytest.fixture
def empty_db():
    return {}


def test_add_task(empty_db):
    result = add_task(empty_db, "Study pytest")
    assert "1" in result
    assert result["1"]["description"] == "Study pytest"
    assert result["1"]["status"] == "todo"
    assert len(empty_db) == 1
