from typing import List, Tuple, Any

from pydantic import BaseModel, validator

from src.models.lesson import Lesson


class StudentModel(BaseModel):
    name: str
    group: str
    lessons: List[Lesson]

    def to_table_row(self) -> Tuple[Any, ...]:
        return (
            self.name,
            self.group,
            str(self.lessons[0]),
            str(self.lessons[1]),
            str(self.lessons[2]),
        )
