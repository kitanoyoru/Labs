from enum import Enum
from typing import List, Dict, Any

from .lesson import Lesson


class StudentFields(Enum):
    NAME = "name"
    GROUP = "group"
    LESSONS = "lessons"


class Student:
    def __init__(self, name: str, group: str, lessons: List[Lesson]) -> None:
        self._name = name
        self._group = group
        self._lessons = lessons

    def to_dict(self) -> Dict[str, Any]:
        d = dict()

        d[StudentFields.NAME.value] = self._name
        d[StudentFields.GROUP.value] = self._group
        d[StudentFields.LESSONS.value] = [lesson.to_dict() for lesson in self._lessons]

        return d

    def from_dict(self, d: Dict[str, Any]) -> None:
        self._name = d[StudentFields.NAME.value]
        self._group = d[StudentFields.GROUP.value]
        self._lessons = [lesson.from_dict() for lesson in d[StudentFields.LESSONS.value]]


