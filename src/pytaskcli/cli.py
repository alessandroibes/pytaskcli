import argparse

from pytaskcli import core


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="PyTaskCLI: A simple command-line task manager"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Command: add
    add = subparsers.add_parser("add", help="Add a new task")
    add.add_argument("description", help="Description of the task")

    # Command: update
    update = subparsers.add_parser("update", help="Update a task")
    update.add_argument("id", help="ID of the task to update")
    update.add_argument("description", help="New description for the task")

    # Command: delete
    delete = subparsers.add_parser("delete", help="Delete a task")
    delete.add_argument("id", help="ID of the task to delete")

    # Command: mark-done
    done = subparsers.add_parser("mark-done", help="Mark a task as done")
    done.add_argument("id", help="ID of the task")

    # Command: mark-in-progress
    progress = subparsers.add_parser("mark-in-progress", help="Mark a task as in-progress")
    progress.add_argument("id", help="ID of the task")

    # Command: list
    list_cmd = subparsers.add_parser("list", help="List tasks")
    list_cmd.add_argument(
        "--status", "-s",
        choices=["all", "todo", "in-progress", "done"],
        default="all",
        help="Filter tasks by status (default: all)"
    )

    return parser


def dispatch_command(args, database):
    if args.command == "add":
        return core.add_task(database, args.description)
    
    elif args.command == "update":
        return core.update_task(database, args.id, args.description)

    elif args.command == "delete":
        return core.delete_task(database, args.id)

    elif args.command == "mark-done":
        return core.change_status(database, args.id, "done")

    elif args.command == "mark-in-progress":
        return core.change_status(database, args.id, "in-progress")

    elif args.command == "list":
        status = None if args.status == "all" else args.status
        return core.list_tasks(database, status)

    else:
        raise ValueError("Unknown command")
