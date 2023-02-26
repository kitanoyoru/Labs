from typing import List

from pymongo.collection import Collection

from src.models.student import Student, StudentFields


class StudentsRepository:
    def __init__(self, col: Collection) -> None:
        self._handler = col 

    def find_by_group(self, group: str) -> List[Student]:
        filter = {
            StudentFields.GROUP.value: group
        }
        data = self._handler.find(filter=filter)

        students = [Student().from_dict(**raw) for raw in data]

        return students

    def find_by_avg(self, avg: float) -> List[Student]:
        filter = {
            "lessons.avg": {
                "$eq": avg
            }
        }
        data = self._handler.find(filter=filter)

        students = [Student().from_dict(**raw) for raw in data]

        return students


    def find_by_name(self, name: str) -> List[Student]:
        filter = {
            "lessons.name": {
                "$eq": name
            }
        }
        data = self._handler.find(filter=filter)

        students = [Student().from_dict(**raw) for raw in data]

        return students

    def find_by_min_score(self, min: float) -> List[Student]:
        filter = {
            "lessons.min": {
                "$eq": min
            }
        }
        data = self._handler.find(filter=filter)

        students = [Student().from_dict(**raw) for raw in data]

        return students

    def find_by_max_score(self, max: float) -> List[Student]:
        filter = {
            "lessons.max": {
                "$eq": max
            }
        }
        data = self._handler.find(filter=filter)

        students = [Student().from_dict(**raw) for raw in data]

        return students
