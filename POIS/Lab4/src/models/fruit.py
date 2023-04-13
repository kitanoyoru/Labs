from pydantic.dataclasses import dataclass

from src.models.tree import Tree


@dataclass
class Fruit:
    name: str
    tree: Tree
    is_growth: bool
    current_growth: float = 0.0