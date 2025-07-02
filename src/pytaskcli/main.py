import sys

from tabulate import tabulate

from pytaskcli.cli import get_parser, dispatch_command
from pytaskcli.db import load_database, save_database


def main():
    parser = get_parser()
    args = parser.parse_args()

    database = load_database()

    try:
        result = dispatch_command(args, database)
    except KeyError:
        sys.exit("Error: Task not found for the provided ID.")
    except Exception as e:
        sys.exit(f"Unexpected error: {e}")

    save_database(database)

    # Display output if any
    if isinstance(result, dict):
        print(tabulate(result.values(), headers="keys", tablefmt="rounded_grid"))
    elif isinstance(result, list):
        if result:
            print(tabulate(result, headers="keys", tablefmt="rounded_grid"))
        else:
            print("Nothing to display.")
