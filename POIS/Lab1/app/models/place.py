import jsonpickle

from abc import ABC, abstractmethod

from typing import List

from .actions import Action, ActionType
from .seed import Seed
from .tree import Tree, AppleTree
from .fruit import Fruit, AppleFruit


class Place(ABC):
    @abstractmethod
    def handle_action(self, action: Action) -> None:
        pass

    @abstractmethod
    def toJson(self) -> str:
        pass


class FruitGarden(Place):
    def __init__(self, seeds: List[Seed]) -> None:
        self._seeds = seeds
        self._trees: List[Tree] = []
        self._fruits: List[Fruit] = []

    def handle_action(self, action: Action) -> None:
        action_type: ActionType = action.get_type()

        match action_type:
            case ActionType.DROUGHT:
                self._cb_on_drought()

    def _cb_on_drought(self) -> None:
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
        json = jsonpickle.encode(self, sort_keys=True, indent=4)
        return json


class VegetableGarden:
    def __init__(self) -> None:
        pass