import jsonpickle

from abc import ABC, abstractmethod


class Seed(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def is_growth(self) -> bool:
        pass

    @abstractmethod
    def cb_ob_drought(self) -> None:
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

        self._current_growth = 0
        self._is_growth: bool = False

    def get_name(self) -> str:
        return self._name

    def is_growth(self) -> bool:
        return self._is_growth

    def cb_ob_drought(self) -> None:
        self._current_growth += self._grow_speed
        if self._current_growth > 10:
            self._is_growth = True

    def get_initial_grow_speed(self) -> float:
        return self._grow_speed

    def toJSON(self) -> str:
        frozen = jsonpickle.encode(self, sort_keys=True, indent=4)


class TomatoSeed(Seed):
    def __init__(self) -> None:
        _name: str = "tomato" 
        _grow_speed: float = 5.4 

    def get_name(self) -> str:
        return self._name

    def get_initial_grow_speed(self) -> float:
        return self._grow_speed

    def toJSON(self) -> str:
        frozen = jsonpickle.encode(self, sort_keys=True, indent=4)