from abc import ABC, abstractmethod

from enum import Enum
from typing import Dict, Any

from .actions import Action, ActionType


class Seed(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def is_growth(self) -> bool:
        pass

    @abstractmethod
    def handle_action(self, action: Action) -> None:
        pass

    @abstractmethod
    def get_initial_grow_speed(self) -> float:
        pass

    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        pass


class AppleSeedFields(Enum):
    NAME = "name"
    GROW_SPEED = "grow_speed"
    CURRENT_GROWTH = "current_growth"
    IS_GROWTH = "is_growth"


class AppleSeed(Seed):
    def __init__(self) -> None:
        self._name: str = "apple"
        self._grow_speed: float = 2.1 

        self._current_growth: float = 0
        self._is_growth: bool = False

    def get_name(self) -> str:
        return self._name

    def get_initial_grow_speed(self) -> float:
        return self._grow_speed

    def is_growth(self) -> bool:
        return self._is_growth

    def handle_action(self, action: Action) -> None:
        action_type: ActionType = action.get_type()

        match action_type:
            case ActionType.DROUGHT:
                self._cb_on_drought()

    def _cb_on_drought(self) -> None:
        self._current_growth += self._grow_speed
        if self._current_growth > 10:
            self._is_growth = True

    def to_dict(self) -> Dict[str, Any]:
        d = dict()

        d[AppleSeedFields.NAME.value] = self._name
        d[AppleSeedFields.GROW_SPEED.value] = self._grow_speed
        d[AppleSeedFields.CURRENT_GROW.value] = self._current_growth
        d[AppleSeedFields.IS_GROWTH.value] = self._is_growth

        return d



class TomatoSeed(Seed):
    def __init__(self) -> None:
        self._name: str = "tomato" 
        self._grow_speed: float = 5.4 

        self._current_growth: float = 0
        self._is_growth: bool = False

    def get_name(self) -> str:
        return self._name

    def get_initial_grow_speed(self) -> float:
        return self._grow_speed

    def is_growth(self) -> bool:
        return self._is_growth

    def handle_action(self, action: Action) -> None:
        action_type: ActionType = action.get_type()

        match action_type:
            case ActionType.DROUGHT:
                self._cb_on_drought()

    def _cb_on_drought(self) -> None:
        self._current_growth += self._grow_speed
        if self._current_growth > 10:
            self._is_growth = True

    def toJSON(self) -> str:
        json = jsonpickle.encode(self, sort_keys=True, indent=4)
        return json