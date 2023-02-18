import jsonpickle

from abc import ABC, abstractmethod

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
    def toJSON(self) -> str:
        pass


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

    def _cb_on_drought(self) -> 'None':
        if self._tree.is_growth():
            self._current_growth += self._tree.get_seed().get_initial_grow_speed()
            if self._current_growth > 10:
                self._is_growth = True            

    def toJSON(self) -> str:
        json: str = jsonpickle.encode(self, sort_keys=True, indent=4)
        return json