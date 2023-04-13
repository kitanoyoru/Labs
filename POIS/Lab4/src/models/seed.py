from pydantic.dataclasses import dataclass

from src.models.tree import Tree


@dataclass
class Seed:
    name: str
    grow_speed: float
    current_growth: float
    is_growth: bool
    is_wilt: bool