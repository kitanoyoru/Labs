from enum import Enum
from typing import Dict, Any


class LessonFields(Enum):
    NAME = "name"
    MIN = "min"
    MAX = "max"
    AVG = "avg"


class Lesson:
    def __init__(self, name: str, min: float, max: float) -> None:
        self._name = name
        self._min = min
        self._max = max

    def to_dict(self) -> Dict[str, Any]:
        d = dict()

        d[LessonFields.NAME.value] = self._name
        d[LessonFields.MIN.value] = self._min
        d[LessonFields.MAX.value] = self._max
        d[LessonFields.AVG.value] = self._find_avg_score()

        return d

    def from_dict(self, d: Dict[str, Any]) -> None:
        self._name = d[LessonFields.NAME.value]
        self._min = d[LessonFields.MIN.value]
        self._max = d[LessonFields.MAX.value]

    def _find_avg_score(self) -> float:
        return (self._max + self._min) / 2
