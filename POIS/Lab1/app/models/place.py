from abc import ABC, abstractmethod

from enum import Enum
from typing import List, Dict, Optional

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


class PlaceFields(Enum):
    SEEDS = "seeds"
    TREES = "trees"
    FRUITS = "fruits"


class FruitGarden:
    def __init__(self, seeds: List[Seed]=[], trees: List[Seed]=[], fruits: List[Seed]=[]) -> None:
        self._seeds: Optional[List[Seed]] = seeds
        self._trees: Optional[List[Tree]] = trees
        self._fruits: Optional[List[Fruit]] = fruits

    def handle_action(self, action: Action) -> None:
        action_type: ActionType = action.get_type()

        match action_type:
            case ActionType.IRRIGATION:
                self._cb_on_irrigation()
            case ActionType.DROUGHT:
                self._cb_on_drought()

    def _cb_on_irrigation(self) -> None:
        for i, seed in enumerate(self._seeds):
            seed._cb_on_irrigation()
            if seed.is_growth():
                tree = AppleTree(seed)
                self._trees.append(tree) # TODO: Delete seed from _seeds
                self._seeds.pop(i)

        for i, tree in enumerate(self._trees):
            tree._cb_on_irrigation()
            if tree.is_growth():
                fruit = AppleFruit(tree)
                self._fruits.append(fruit)
                self._trees.pop(i)

        for fruit in self._fruits:
            fruit._cb_on_irrigation()

    def _cb_on_drought(self) -> None:
        for i, seed in enumerate(self._seeds):
            seed._cb_on_drought()
            if seed.is_wilt():
                self._seeds.pop(i)

        for i, tree in enumerate(self._trees):
            tree._cb_on_drought()
            if tree.is_wilt():
                self._trees.pop(i)

        for i, fruit in enumerate(self._fruits):
            fruit._cb_on_is_wilt()
            if fruit.is_wilt():
                self._fruits.pop(i)

    def to_dict(self) -> Dict[str, dict]:
        d = dict()

        d[PlaceFields.SEEDS.value] = [seed.to_dict() for seed in self._seeds]
        d[PlaceFields.TREES.value] = [tree.to_dict() for tree in self._trees]
        d[PlaceFields.FRUITS.value] = [fruit.to_dict() for fruit in self._fruits]

        return d
