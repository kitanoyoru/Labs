from dataclasses import dataclass

@dataclass
class MongoConfig:
    url: str = "mongodb://localhost:27017/game"
    db: str = "game"