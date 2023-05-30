from abc import ABC, abstractmethod

from functools import total_ordering, reduce

from typing import List, Optional

from lab8.utils import convert_to_bytes, sum_two_bin

from lab8.constants import MATRIX_SIZE


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
    def __init__(self, value: Optional[int] = None) -> None:
        if value is not None:
            self._bytes = convert_to_bytes(value)
        else:
            self._bytes = []

    @classmethod
    def from_bytes(self, bytes: List[int]) -> None:
        w = Word()
        w._bytes = bytes
        return w

    def push_byte(self, byte: int) -> None:
        self._bytes.append(byte)

    def __getitem__(self, key):
        return self._bytes[key]

    def __setitem__(self, key, value):
        self._bytes[key] = value

    def __repr__(self) -> str:
        return str(self._bytes)

    def __eq__(self, value: "Word") -> bool:
        return self._bytes == value._bytes

    def __lt__(self, value: "Word") -> bool:
        return self._bytes < value._bytes


class Memory:
    def __init__(self) -> None:
        self._memory = [[0 for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)] 

    def write(self, val: int, address: int) -> None:
        word = Word(val)
        return self._write_word(word, address)

    def _write_word(self, word: Word, address: int) -> None:
        for i in range(address, MATRIX_SIZE):
            self._memory[i][address] = word[i-address] 

        for i in range(address):
            self._memory[i][address] = word[MATRIX_SIZE-address+i]


    def read(self, address: int) -> Word:
        return self._read_word(address)

    def _read_word(self, address: int) -> Word:
        word = Word()

        for i in range(address, MATRIX_SIZE):
            word.push_byte(self._memory[i][address])

        for i in range(address):
            word.push_byte(self._memory[i][address])

        return word

    def get_normal_matrix(self) -> List[Word]:
        return [self._read_word(addr) for addr in range(MATRIX_SIZE)] 

    def to_diagonal_matrix(self, from_matrix: Optional[List[Word]] = None) -> None:
        if from_matrix is None:
            from_matrix = self.get_normal_matrix()

        for i in range(MATRIX_SIZE):
            self._write_word(from_matrix[i], i)

    def sum(self, v: List[int]) -> None:
        for i in range(MATRIX_SIZE):
            curr_word = self._read_word(i)
            vj = curr_word._bytes[:3]

            if vj == v:
                curr_word._bytes[11:] = sum_two_bin(curr_word._bytes[3:7], curr_word._bytes[7:11])
                self._write_word(curr_word, i)

    def func_2(self, addr_1: int, addr_2: int, res_addr: int) -> None:
        bool_func = "{0} and (not {1})"
        self._func(bool_func, addr_1, addr_2, res_addr)

    def func_7(self, addr_1: int, addr_2: int, res_addr: int) -> None:
        bool_func = "{0} or {1}"
        self._func(bool_func, addr_1, addr_2, res_addr)

    def func_8(self, addr_1: int, addr_2: int, res_addr: int) -> None:
        bool_func = "not ({0} or {1})"
        self._func(bool_func, addr_1, addr_2, res_addr)

    def func_13(self, addr_1: int, addr_2: int, res_addr: int) -> None:
        bool_func = "(not {0}) or {1})"
        self._func(bool_func, addr_1, addr_2, res_addr)

    def _func(self, bool_func: str, addr_1: int, addr_2: int, res_addr: int) -> None:
        word_1, word_2 = map(self._read_word, (addr_1, addr_2))

        res_bytes = [int(eval(bool_func.format(word_1[i], word_2[i]))) for i in range(MATRIX_SIZE)]
        res_word = Word.from_bytes(res_bytes)

        self._write_word(res_word, res_addr)


    def in_range(self, lower: int, upper: int) -> List[Word]:
        lower_word, upper_word = map(Word, (lower, upper))
        def check_in_range(acc: List[Word], word: Word) -> List[Word]:
            if lower_word < word and upper_word > word:
                acc.append(word) 

            return acc

        return reduce(check_in_range, (self.read(i) for i in range(MATRIX_SIZE)), [])

    def __str__(self) -> str:
        return str([self._read_word(addr) for addr in range(MATRIX_SIZE)])

        





    

