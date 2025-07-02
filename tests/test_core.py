import pytest

from src.core import (
    add_task,
    change_status,
    delete_task,
    list_tasks,
    TaskStatus,
    update_task
)


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


def test_update_task_invalid_id(empty_db):
    with pytest.raises(KeyError):
        update_task(empty_db, "42", "Fail")


def test_delete_task(empty_db):
    add_task(empty_db, "Delete later")
    deleted = delete_task(empty_db, "1")
    assert deleted["1"]["description"] == "Delete later"
    assert "1" not in empty_db


def test_delete_task_invalid_id(empty_db):
    with pytest.raises(KeyError):
        delete_task(empty_db, "99")


@pytest.mark.parametrize("status", ["in-progress", "done", "todo"])
def test_change_status(empty_db, status: TaskStatus):
    add_task(empty_db, "Test status")
    result = change_status(empty_db, "1", status)
    assert result["1"]["status"] == status


def test_change_status_invalid_id(empty_db):
    with pytest.raises(KeyError):
        change_status(empty_db, "99", "done")


def test_list_tasks_all(empty_db):
    add_task(empty_db, "A")
    add_task(empty_db, "B")
    change_status(empty_db, "2", "done")
    all_tasks = list_tasks(empty_db)
    assert len(all_tasks) == 2


def test_list_tasks_filtered(empty_db):
    add_task(empty_db, "Task 1")
    add_task(empty_db, "Task 2")
    change_status(empty_db, "2", "done")
    done = list_tasks(empty_db, status_filter="done")
    assert len(done) == 1
    assert done[0]["status"] == "done"
