from src.game import Game

from src.config.mongo import MongoConfig
from src.repository import StateRepository
from src.storage.mongo import MongoStorage

class App:
    def __init__(self) -> None:
        _config = MongoConfig()
        _db = MongoStorage(_config)
        _repository = StateRepository(_db.score_handler()) 

        self._game = Game(_repository)

    def run(self) -> None:
        self._game.run()
