import argparse
from task_controller import (create_task, update_task, delete_task, mark_in_progress, mark_done, list_tasks)

def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", type=str, help="Task description")

    # Update
    parser_update = subparsers.add_parser("update", help="Update a tasks description by its id")
    parser_update.add_argument("id", type=int, help="Task ID")
    parser_update.add_argument("description", type=str, help="Task description")

    # Delete
    parser_delete = subparsers.add_parser("delete", help="Delete a task by its id")
    parser_delete.add_argument("id", type=int, help="Task ID")

    # Mark in progress
    parser_inprogress = subparsers.add_parser("mark-in-progress", help="Update task's status to in progress")
    parser_inprogress.add_argument("id", type=int, help="Task ID")

    # Mark done
    parser_done = subparsers.add_parser("mark-done", help="Update task's status to done")
    parser_done.add_argument("id", type=int, help="Task ID")

    parser_list = subparsers.add_parser("list", help="List tasks")
    parser_list.add_argument("status", nargs="?", choices=["done", "todo", "in-progress"], help="Filter by status")


    args = parser.parse_args()

    if args.command == "add":
        create_task(args.description)
    elif args.command == "update":
        update_task(args.id, args.description)
    elif args.command == "delete":
        delete_task(args.id)
    elif args.command == "mark-in-progress":
        mark_in_progress(args.id)
    elif args.command == "mark-done":
        mark_done(args.id)
    elif args.command == "list":
        list_tasks(args.status)
    else:
        parser.print_help()
        
if __name__ == "__main__":
    main()