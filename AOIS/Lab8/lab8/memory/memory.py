from abc import ABC


from lab8.constants import MATRIX_SIZE




class IMemory(ABC):
    pass


class Word:
    def __init__(self, value)


class Memory:
    def __init__(self) -> None:
        self._memory = [[0 for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)] 

    def __lt__(self, other: Memory)
