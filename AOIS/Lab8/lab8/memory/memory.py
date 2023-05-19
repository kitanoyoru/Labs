from abc import ABC

from functools import total_ordering


from lab8.constants import MATRIX_SIZE
from lab8.utils import convert_to_bytes




class IMemory(ABC):
    pass


class Word:
    def __init__(self, value: int) -> None:
        self._bytes = convert_to_bytes(value)

    def __repr__(self) -> str:
        return str(self._bytes)

    def __eq__(self, other: "Word") -> bool:
        return self._bytes == other._bytes 

    def __lt__(self, other: "Word") -> bool:
        g, l = False, False

        for i in range(self._bytes) 



class Memory:
    def __init__(self) -> None:
        self._memory = [[0 for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)] 

    def __lt__(self, other: Memory)
