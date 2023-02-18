import jsonpickle

from abc import ABC, abstractmethod

from .seed import Seed

class Vegetable(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_seed(self) -> Seed:
        pass

    @abstractmethod
    def toJSON(self) -> str:
        pass


class Tomato(Vegetable):
    def __init__(self) -> None:
        self._name = "tomato"
        self._seed = TomatoSeed()

        self._current_growth = 0 
        self._is_growth = False

    def get_seed(self) -> Seed:
        return self._seed

    def cb_on_drought(self) -> None:
        self._current_growth += self._seed.get_initial_grow_speed()
        if self._current_growth == 10:
            self._is_growth = True

    def toJSON(self) -> str:
        frozen = jsonpickle.encode(self, sort_keys=True, indent=4)