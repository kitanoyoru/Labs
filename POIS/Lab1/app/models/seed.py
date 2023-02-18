import jsonpickle

from abc import ABC, abstractmethod

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
    def toJSON(self) -> str:
        pass


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


    def toJSON(self) -> str:
        json: str = jsonpickle.encode(self, sort_keys=True, indent=4)
        return json 


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

        match ation_type:
            case ActionType.DROUGHT:
                self._cb_on_drought()

    def _cb_on_drought(self) -> None:
        self._current_growth += self._grow_speed
        if self._current_growth > 10:
            self._is_growth = True

    def toJSON(self) -> str:
        json = jsonpickle.encode(self, sort_keys=True, indent=4)
        return json