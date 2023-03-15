from typing import List, Optional


from bson import ObjectId
from pymongo.collection import Collection
from pydantic import BaseModel, validator

from src.models.student import StudentModel


class StudentFilterOptions(BaseModel):
    name: Optional[str]
    group: Optional[str]
    max: Optional[float]
    min: Optional[float]
    avg: Optional[float]

    @validator("max", "min", "avg", pre=True)
    def parse_to_float(cls, value: Optional[str]) -> Optional[float]:
        if value is not None:
            return abs(float(value))
        return value


class StudentsRepository:
    def __init__(self, col: Collection) -> None:
        self._handler = col

    def list_all_students(self) -> List[StudentModel]:
        data = self._handler.find()
        students = [StudentModel(**raw) for raw in data]
        return students

    def add_student(self, student: StudentModel):
        data = student.dict()
        self._handler.insert_one(data)

    def delete_student(self, name: str):
        self._handler.delete_one({"name": name})

    def filter_student(self, opts: StudentFilterOptions) -> List[StudentModel]:
        filtered = list()

        if opts.name is not None:
            items = self._filter_by_name(opts.name)
            filtered.extend(items)
        if opts.group is not None:
            items = self._filter_by_group(opts.group)
            filtered.extend(items)
        if opts.max is not None:
            items = self._filter_by_max_score(opts.max)
            filtered.extend(items)
        if opts.min is not None:
            items = self._filter_by_min_score(opts.min)
            filtered.extend(items)
        if opts.avg is not None:
            items = self._filter_by_avg_score(opts.avg)
            filtered.extend(items)

        return filtered

    def _filter_by_group(self, group: str) -> List[StudentModel]:
        filter = {"group": group}
        data = self._handler.find(filter=filter)

        students = [StudentModel(**raw) for raw in data]

        return students

    def _filter_by_avg_score(self, avg: float) -> List[StudentModel]:
        filter = {"lessons.avg": {"$eq": avg}}
        data = self._handler.find(filter=filter)

        students = [StudentModel(**raw) for raw in data]

        return students

    def _filter_by_name(self, name: str) -> List[StudentModel]:
        filter = {"lessons.name": {"$eq": name}}
        data = self._handler.find(filter=filter)

        students = [StudentModel(**raw) for raw in data]

        return students

    def _filter_by_min_score(self, min: float) -> List[StudentModel]:
        filter = {"lessons.min": {"$eq": min}}
        data = self._handler.find(filter=filter)

        students = [StudentModel(**raw) for raw in data]

        return students

    def _filter_by_max_score(self, max: float) -> List[StudentModel]:
        filter = {"lessons.max": {"$eq": max}}
        data = self._handler.find(filter=filter)

        students = [StudentModel(**raw) for raw in data]

        return students
