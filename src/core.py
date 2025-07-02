from datetime import datetime


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
