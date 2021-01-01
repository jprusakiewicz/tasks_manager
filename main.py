from datetime import datetime
import argparse
import sys
# from task import Task
from task import TaskModel
from task_manager import TaskManager


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', type=str)
    # parser.add_argument('--task_hash', type=str)
    parser.add_argument('--name', type=str)
    parser.add_argument('--deadline', type=str)
    parser.add_argument('--description', type=str)
    parser.add_argument('--hash', type=str)
    args = parser.parse_args()

    action = args.action.lower()
    task_model = TaskModel(name=args.name, deadline=args.deadline, description=args.description)

    if action == "add":
        TaskManager.add(task_model)
    elif action == "upadte":
        TaskManager.update(task_model, args.task_hash)
    elif action == "list":
        list = TaskManager.list(...)
        print(list)
    elif action == "remove":
        TaskManager.remove(args.task_hash)


if __name__ == "__main__":
    main()
