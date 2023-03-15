from pydantic import BaseModel, validator

from typing import List, Union, Optional


class Lesson(BaseModel):
    name: str
    max_score: float
    min_score: float
    avg_score: float

    @validator("max_score", "min_score", pre=True)
    def validate_max_score(cls, value: Union[str, float]) -> float:
        value = float(value) if isinstance(value, str) else value
        return abs(value)

    @classmethod
    def from_text(cls, data: str) -> List["Lesson"]:
        """
        math 3 10 | rus 5 8 | eng 1 10
        """
        raw_lessons = [x.strip().split(" ") for x in data.split("|")]
        lessons = list()

        for args in raw_lessons:
            name, max_score, min_score = args[0], float(args[1]), float(args[2])
            avg_score = (max_score + min_score) / 2
            lesson = cls(
                name=name, max_score=max_score, min_score=min_score, avg_score=avg_score
            )
            lessons.append(lesson)

        return lessons

    def __str__(self) -> str:
        return f"{self.name} {self.max_score} {self.min_score} {self.avg_score}"
