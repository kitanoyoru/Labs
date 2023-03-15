from typing import List, Tuple, Any

from pydantic import BaseModel, validator

from src.models.exam import Exam


class StudentModel(BaseModel):
    name: str
    group: str
    exams: List[Exam]

    def to_table_row(self) -> Tuple[Any, ...]:
        return (
            self.name,
            self.group,
            str(self.exams[0]),
            str(self.exams[1]),
            str(self.exams[2]),
        )
