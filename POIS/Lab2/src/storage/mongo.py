from pymongo import MongoClient

from src.config.storage import StorageConfig
from src.repositories import StudentRepository


class MongoStorage:
    def __init__(self, config: StorageConfig) -> None:
        self._client: MongoClient = MongoClient(config.Url)
        self._db = self._client.get_database(config.StudentsCollection)

        self._studentsCollection = self._db.get_collection(config.StudentsCollection)
        self.handleStudents = StudentRepository(self._studentsCollection)
