from abc import ABC, abstractmethod

from enum import Enum
from typing import Dict, Any

from .tree import Tree
from .actions import Action, ActionType


class Fruit(ABC):
    @abstractmethod
    def get_tree(self) -> Tree:
        pass

    @abstractmethod
    def handle_action(self, action: Action) -> None:
        pass

    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        pass


class AppleFruitFields(Enum):
    TREE = "tree"
    CURRENT_GROWTH = "current_growth"
    IS_GROWTH = "is_growth"


class AppleFruit:
    def __init__(self, tree: Tree) -> None:
        self._tree = tree

        self._current_growth = 0
        self._is_growth = False

    def get_tree(self) -> Tree:
        return self._tree

    def handle_action(self, action: Action) -> None:
        action_type: ActionType = action.get_type()

        match action_type:
            case ActionType.DROUGHT:
                self._cb_on_drought()

    def _cb_on_drought(self) -> "None":
        if self._tree.is_growth():
            self._current_growth += self._tree.get_seed().get_initial_grow_speed()
            if self._current_growth > 10:
                self._is_growth = True

    def to_dict(self) -> Dict[str, Any]:
        d = dict()

        d[AppleFruitFields.TREE.value] = self._tree.to_dict()
        d[AppleFruitFields.CURRENT_GROWTH.value] = self._current_growth
        d[AppleFruitFields.IS_GROWTH.value] = self._is_growth

        return d
