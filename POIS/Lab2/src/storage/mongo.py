import pymongo

from .istorage import IStorage
from src.config.storage import StorageConfig
from src.repositories import StudentsRepository 

class MongoStorage(IStorage):
    def __init__(self, config: StorageConfig) -> None:
        self._client = pymongo.MongoClient(config.Url)
        self._db = self._client.get_database(config.StudentsCollection) 

        self._studentsCollection = self._db.get_collection(config.StudentsCollection) 
        self.handleStudents = StudentsRepository(self._studentsCollection)


    
