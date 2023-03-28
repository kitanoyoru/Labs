from typing import Dict, Any, Optional

from pymongo.collection import Collection


class StateRepository:
    def __init__(self, connection: Collection) -> None:
        self._connection = connection

    def save_score(self, record: Dict[str, Any]):
        self._connection.insert_one(document=record)

    def read_last_score(self) -> Optional[Dict[str, Any]]:
        return self._connection.find_one(projection={"_id": False})