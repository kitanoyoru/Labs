import jsonpickle
from abc import ABC, abstractmethod

from .seed import AppleSeed, Seed

class Tree(ABC):
    @abstractmethod
    def get_seed(self) -> 'Seed':
        pass

    @abstractmethod
    def is_growth(self) -> bool:
        pass

    @abstractmethod
    def cb_on_drought(self) -> None:
        pass
    
    @abstractmethod
    def toJSON(self) -> str:
        pass


class AppleTree(Tree):
    def __init__(self, seed: AppleSeed) -> None:
        self._seed = seed 

        self._current_growth = 0 
        self._is_growth = False

    def get_seed(self) -> Seed:
        return self._seed
    
    def is_growth(self) -> bool:
        return self._is_growth

    def cb_on_drought(self) -> None:
        self._current_growth += self._seed.get_initial_grow_speed()
        if self._current_growth == 10:
            self._is_growth = True

    def toJSON(self) -> str:
        frozen = jsonpickle.encode(self, sort_keys=True, indent=4)