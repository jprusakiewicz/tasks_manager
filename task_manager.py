from typing import List
from datetime import date
from task import Task, TaskModel
import database


def is_date_today(date_to_check: str):
    return date.fromisoformat(date_to_check) == date.today()


class TaskManager:
    @staticmethod
    def add(task_model: TaskModel):
        task = Task(task_model.name, task_model.deadline, task_model.description)
        task_model.hash = task.hash_value
        d = task_model.dict()
        database.add(d)

    @staticmethod
    def update(task_model: TaskModel, hash_value: str):
        task = Task(task_model.name, task_model.deadline, task_model.description)
        task_model.hash = task.hash_value
        database.update(task_model, hash_value)

    @staticmethod
    def list(task_filter: str) -> List[dict]:
        all_tasks = database.get_all()
        if task_filter == "today":
            return TaskManager._filter_tasks(all_tasks)
        return all_tasks

    @staticmethod
    def remove(hash_value: str):
        database.remove(hash_value)

    @staticmethod
    def _filter_tasks(tasks) -> List[dict]:
        return [t for t in tasks if is_date_today(t['deadline'])]
