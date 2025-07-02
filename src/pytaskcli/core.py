from datetime import datetime
from typing import Literal, Optional
from .utils import format_datetime


TaskStatus = Literal["todo", "in-progress", "done"]
Task = dict[str, str]
Database = dict[str, Task]


def generate_new_id(database: Database) -> str:
    return str(int(max(["0"] + list(database.keys()))) + 1)


def create_task(description: str) -> Task:
    now = datetime.now().isoformat()
    return {
        "description": description,
        "status": "todo",
        "created-at": now,
        "updated-at": now,
    }


def add_task(database: Database, description: str) -> Task:
    task_id = generate_new_id(database)
    task = create_task(description)
    database[task_id] = task
    return {task_id: task}


def update_task(database: Database, task_id: str, description: str) -> Task:
    task = database[task_id]
    task["description"] = description
    task["updated-at"] = datetime.now().isoformat()
    return {task_id: task}


def delete_task(database: Database, task_id: str) -> Task:
    task = database.pop(task_id)
    return {task_id: task}


def change_status(database: Database, task_id: str, status: TaskStatus) -> Task:
    task = database[task_id]
    task["status"] = status
    task["updated-at"] = datetime.now().isoformat()
    return {task_id: task}


def list_tasks(database: Database, status_filter: Optional[TaskStatus] = None) -> list[dict]:
    tasks = []
    for task_id, task in sorted(database.items(), key=lambda t: int(t[0])):
        if status_filter is None or task["status"] == status_filter:
            tasks.append({
                "id": task_id,
                "description": task["description"],
                "status": task["status"],
                "created At": format_datetime(task["created-at"]),
                "updated At": format_datetime(task["updated-at"]),
            })
    return tasks
