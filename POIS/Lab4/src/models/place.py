from pydantic.dataclasses import dataclass

from typing import List

from .seed import Seed
from .tree import Tree
from .fruit import Fruit


@dataclass
class Place:
    seeds: List[Seed]
    trees: List[Tree]
    fruits: List[Fruit]

