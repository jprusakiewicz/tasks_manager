import argparse
from task import TaskModel
from task_manager import TaskManager


def main():
    args = parse_arguments()
    execute_command(args)


def execute_command(args):
    option = args.option.lower()
    if option == "add":
        task_model = TaskModel(name=args.name, deadline=args.deadline, description=args.description)
        TaskManager.add(task_model)
    elif option == "update":
        task_model = TaskModel(name=args.name, deadline=args.deadline, description=args.description)
        TaskManager.update(task_model, args.task_hash)
    elif option == "list":
        tasks = TaskManager.list(args.filter)
        print(tasks)
    elif option == "remove":
        TaskManager.remove(args.task_hash)


def parse_arguments():
    parser = argparse.ArgumentParser(description="manage your tasks")
    parser.add_argument('option', choices=['add', 'update', 'list', 'remove'], type=str, help="action")
    parser.add_argument('--name', type=str, help="task name")
    parser.add_argument('--deadline', type=str, required=False, help="format: yyyy-mm-dd")
    parser.add_argument('--description', type=str, required=False, help="task description")
    parser.add_argument('--filter', type=str, choices=["all", "today"], help="filter listed items by date")
    parser.add_argument('--task_hash', type=int)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
