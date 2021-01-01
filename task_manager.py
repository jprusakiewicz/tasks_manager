from datetime import datetime

from task import Task, TaskModel


class TaskManager:
    @staticmethod
    def add(task_model: TaskModel):
        # task = Task(name, deadline, description)
        # database.add
        ...

    @staticmethod
    def update(task_model: TaskModel, hash_value: str):
        ...

    @staticmethod
    def list(task_filter: str) -> TaskModel:
        # all_tasks = database.get_all()
        # filtered_tasks = self._filter_tasks()
        # return filtered_tasks
        ...

    @staticmethod
    def remove(hash_value: str):
        ...

    @staticmethod
    def _filter_tasks(self):
        ...
