from pymongo import MongoClient
from pymongo.collection import Collection

from src.config.mongo import MongoConfig

class MongoStorage:
    def __init__(self, config: MongoConfig) -> None:
        self._client: MongoClient = MongoClient(config.url)
        self._db = self._client.get_database(config.db)

    def score_handler(self) -> Collection:
        return self._db.get_collection("score")
