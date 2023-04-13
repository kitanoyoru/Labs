from pydantic.dataclasses import dataclass

from src.models.seed import Seed


@dataclass
class Tree: 
    name: str
    seed: Seed
    is_growth: bool
    current_growth: float = 0.0