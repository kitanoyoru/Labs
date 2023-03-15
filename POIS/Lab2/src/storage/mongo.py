from pymongo import MongoClient

from src.config.mongo import MongoConfig
from src.repositories import StudentsRepository


class MongoStorage:
    def __init__(self, config: MongoConfig) -> None:
        self._client: MongoClient = MongoClient(config.url)
        self._db = self._client.get_database(config.StudentsCollection)

        self._studentsCollection = self._db.get_collection(config.StudentsCollection)
        self.handleStudents = StudentsRepository(self._studentsCollection)
