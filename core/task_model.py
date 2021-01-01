from pydantic import BaseModel
from datetime import date
from typing import Union


class Task:
    def __init__(self, name: str, deadline: str, description: str):
        if name:
            self.name: str = name
        if deadline:
            self.deadline: date = date.fromisoformat(deadline)
        if description:
            self.description: str = description
        self.hash_value: int = self._calculate_hash_from_self_content()

    def _calculate_hash_from_self_content(self) -> int:
        return hash(self)


class TaskModel(BaseModel):
    name: Union[str, None]
    deadline: Union[str, None]
    description: Union[str, None]
    hash: Union[str, None]
