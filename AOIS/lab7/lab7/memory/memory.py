import re

from abc import ABC, abstractmethod

from functools import total_ordering, reduce

from typing import List, Optional, Type

from lab7.utils import convert_to_bytes, MAX_BYTES


class IMemory(ABC):
    @abstractmethod
    def insert(self, value: int) -> None:
        pass

    @abstractmethod
    def search_by_template(self, reverse: Optional[bool]) -> None:
        pass

    @abstractmethod
    def check_by_bool_func(self, bool_fund: str) -> List["Word"]:
        pass

@total_ordering
class Word:
    def __init__(self, value: int) -> None:
        self._bytes = convert_to_bytes(value)

    def __repr__(self) -> str:
        return str(self._bytes)

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

    def search_by_template(self, template: int, limit: int = 5) -> List[Word]:
        def count_equals_bytes(word: Word) -> int:
            counter = 0
            for i in range(MAX_BYTES):
                if word._bytes[i] == template_word._bytes[i]:
                    counter += 1

            return counter


        template_word = Word(template)
        return sorted(self._words, key=lambda word: count_equals_bytes(word))[:limit]

    def check_by_bool_func(self, bool_func: str) -> List[Word]:
        formatted_bool_func = re.sub(r"[a-zA-Z]", "{}", bool_func)


        def check_word(acc: List[Word], word: Word) -> List[Word]:
            result = eval(formatted_bool_func.format(*word._bytes))

            if result:
              acc.append(word)  

            return acc

            

        return list(reduce(check_word, self._words, []))
                
        
