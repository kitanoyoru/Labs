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
    def is_wilt(self) -> bool:
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


class SeedFields(Enum):
    NAME = "name"
    GROW_SPEED = "grow_speed"
    CURRENT_GROWTH = "current_growth"
    IS_GROWTH = "is_growth"


class AppleSeed(Seed):
    def __init__(self, current_growth: float = 0, is_growth: bool = False, is_wilt: bool = False) -> None:
        self._name: str = "apple"
        self._grow_speed: float = 2.1

        self._current_growth: float = current_growth
        self._is_growth: bool = is_growth
        self._is_wilt: bool = is_wilt

    def get_name(self) -> str:
        return self._name

    def get_initial_grow_speed(self) -> float:
        return self._grow_speed

    def is_growth(self) -> bool:
        return self._is_growth

    def is_wilt(self) -> bool:
        return self._is_wilt

    def handle_action(self, action: Action) -> None:
        action_type: ActionType = action.get_type()

        match action_type:
            case ActionType.IRRIGATION:
                self._cb_on_irrigation()
            case ActionType.DROUGHT:
                self._cb_on_drought()

    def _cb_on_irrigation(self) -> None:
        self._current_growth += self._grow_speed
        if self._current_growth > 10:
            self._is_growth = True

    def _cb_on_drought(self) -> None:
        self._current_growth -= self._grow_speed
        if self._current_growth < 0:
            self._is_growth = False
            self._is_wilt = True

    def to_dict(self) -> Dict[str, Any]:
        d = dict()

        d[SeedFields.NAME.value] = self._name
        d[SeedFields.GROW_SPEED.value] = self._grow_speed
        d[SeedFields.CURRENT_GROWTH.value] = self._current_growth
        d[SeedFields.IS_GROWTH.value] = self._is_growth

        return d
