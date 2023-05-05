from abc import ABC, abstractmethod

from functools import total_ordering, reduce
from typing import List, Optional

from utils import convert_to_bytes


class IMemory(ABC):
    @abstractmethod
    def insert(self, value: int) -> None:
        pass

    @abstractmethod
    def sort(self, reverse: Optional[bool]) -> None:
        pass

    @abstractmethod
    def in_range(self, lower: int, upper: int) -> List[Word]:
        pass

@total_ordering
class Word:
    def __init__(self, value: int) -> None:
        self._bytes = convert_to_bytes(value)

    def __repr__(self) -> str:
        return self._bytes

    def __eq__(self, value: "Word") -> bool:
        return self._bytes == value._bytes

    def __lt__(self, value: "Word") -> bool:
        return self._bytes < value._bytes


class Memory:
    def __init__(self, initial_values: List[int]) -> None:
        self._words: List[Word] = []
        for value in initial_values:
            self.insert(value)

    def insert(self, value: int) -> None:
        w = Word(value)
        self._words.append(w)

    def sort(self, reverse: Optional[bool]) -> None:
        self._words.sort(reverse=reverse)

    def in_range(self, lower: int, upper: int) -> List[Word]:
        def closure(word: Word, acc: List[Word]):
            acc.append(word if word > lower_word and word < upper_word else None) 
            return acc

        lower_word, upper_word = map(Word, (lower, upper))

        return list(filter(reduce(closure, self._words, [])))
        