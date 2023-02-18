import jsonpickle

from abc import ABC, abstractmethod

from typing import List

from .seed import Seed
from .tree import Tree, AppleTree
from .fruit import Fruit, AppleFruit


class FruitGarden:
    def __init__(self, seeds: List[Seed]) -> None:
        self._seeds = seeds
        self._trees: List[Tree] = []
        self._fruits: List[Fruit] = []

    def cb_on_drought(self) -> None:
        for seed in self._seeds:
            seed.cb_on_drought()
            if seed.is_growth():
                tree = AppleTree(seed)
                self._trees.append(tree)

        for tree in self._trees:
            seed.cb_on_drought()
            if tree.is_growth():
                fruit = AppleFruit(tree)
                self._fruits.append(fruit)

        for fruit in self._fruits:
            seed.cb_on_drought()

    def toJSON(self) -> str:
        frozen = jsonpickle.encode(self, sort_keys=True, indent=4)


class VegetableGarden:
    def __init__(self) -> None:
        pass