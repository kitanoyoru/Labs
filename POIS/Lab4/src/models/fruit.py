from pydantic.dataclasses import dataclass

from src.models.tree import Tree


@dataclass
class Fruit:
    name: str
    tree: Tree
    current_growth: float
    is_growth: bool
    is_wilt: bool