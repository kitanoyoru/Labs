from abc import ABC, abstractmethod

from enum import Enum
from typing import List, Dict

from .actions import Action, ActionType
from .seed import Seed
from .tree import Tree, AppleTree
from .fruit import Fruit, AppleFruit


class Place(ABC):
    @abstractmethod
    def handle_action(self, action: Action) -> None:
        pass

    @abstractmethod
    def to_dict(self) -> Dict[str, dict]:
        pass


class FruitGardenFields(Enum):
    SEEDS = "seeds"
    TREES = "trees"
    FRUITS = "fruits"


class FruitGarden:
    def __init__(self, seeds: List[Seed]) -> None:
        self._seeds: List[Seed] = seeds
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

    def to_dict(self) -> Dict[str, dict]:
        d = dict()

        d[FruitGardenFields.SEEDS.value] = [seed.to_dict() for seed in self._seeds]
        d[FruitGardenFields.TREES.value] = [tree.to_dict() for tree in self._trees]
        d[FruitGardenFields.FRUITS.value] = [fruit.to_dict() for fruit in self._fruits]

        return d


class VegetableGarden:
    def __init__(self) -> None:
        pass
