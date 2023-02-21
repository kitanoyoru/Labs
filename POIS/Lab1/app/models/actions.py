from abc import ABC, abstractmethod
from enum import Enum


class ActionType(Enum):
    DROUGHT = 1
    QUIT = 2


class Action(ABC):
    @abstractmethod
    def get_type(self) -> ActionType:
        pass


class Drought:
    def __init__(self) -> None:
        self._type = ActionType.DROUGHT

    def get_type(self) -> ActionType:
        return self._type


class Quit:
    def __init__(self) -> None:
        self._type = ActionType.QUIT

    def get_type(self) -> ActionType:
        return self._type
