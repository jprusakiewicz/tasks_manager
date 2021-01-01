from abc import ABC


class TaskManagerInterface(ABC):
    def add(self):
        ...

    def list(self):
        ...

    def remove(self):
        ...

    def update(self):
        ...
