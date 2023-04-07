from functools import reduce
from dataclasses import dataclass

from typing import Optional, List, Any, Union

import src.table.constants as constants


@dataclass
class BoolVar:
    value: int


    def __hash__(self) -> int:
        return hash(self.value)

    def __eq__(self, __other: object) -> bool:
        is_equals = False

        if isinstance(__other, BoolVar):
            is_equals = self.value == __other.value
        elif isinstance(__other, int):
            is_equals = self.value == __other

        return is_equals

            
# REFACTOR: maybe rafactor it using __slots__
@dataclass
class Row:
    a: Optional[BoolVar]
    b: Optional[BoolVar]
    c: Optional[BoolVar]
    result: Optional[BoolVar] = None

    def __getitem__(self, __key: Union[str, int]) -> Optional[BoolVar]:
        val = None

        if isinstance(__key, str):
            val = getattr(self, __key)
        elif isinstance(__key, int):
            val = getattr(self, chr(97 + __key))
        
        return val

    def __setitem__(self, __key: str, __value: BoolVar) -> None:
        setattr(self, __key, __value)

    def __eq__(self, __other: object) -> bool:
        if isinstance(__other, Row):
            for key in ["a", "b", "c"]:
                if self[key] != __other[key]:
                    return False
            return True

        raise ValueError()

    def __len__(self) -> int:
        return 3

    def __hash__(self) -> int:
        return hash((self.a, self.b, self.c))

    def has_none_field(self) -> bool:
        accumulator = lambda acc, val: acc + int(val is None)
        acc = reduce(accumulator, [getattr(self, key) for key in ["a", "b", "c"]])
        return acc == 1


class Table:
    def __init__(self, formula: str) -> None:
        self._table = self._generate_table(formula)

    def __getitem__(self, index: int) -> Row:
        return self._table[index]

    def _generate_table(self, formula: str) -> List[Row]:
        table: List[Row] = []
        for init_row_data in constants.INIT_TABLE_DATA:
            row_data = [BoolVar(val) for val in init_row_data]
            table.append(Row(*row_data))

        self._fill_table_with_result(formula, table)
        return table

    def _fill_table_with_result(self, formula: str, table: List[Row]) -> None:
        for i in range(constants.TABLE_ROWS):
            table[i].result = Table._get_result(formula, table[i])

    @classmethod
    def _get_result(cls, formula: str, row: Row) -> BoolVar:
        stack: List[int] = []
        polish = cls._polish_notation(formula, row)

        for char in polish:
            if char.isdigit():
                stack.append(char)
            elif char == "!":
                x, handler = stack.pop(), constants.OPERATION_HANDLERS[char]
                stack.append(handler(x))
            elif char == "&":
                a, b, handler = (
                    stack.pop(),
                    stack.pop(),
                    constants.OPERATION_HANDLERS[char],
                )
                stack.append(handler(a, b))
            elif char == "|":
                a, b, handler = (
                    stack.pop(),
                    stack.pop(),
                    constants.OPERATION_HANDLERS[char],
                )
                stack.append(handler(a, b))

        result = BoolVar(stack.pop())

        return result

    @classmethod
    def _polish_notation(cls, formula: str, row: Row) -> List[str]:
        stack, result = [], []

        for char in ["a", "b", "c"]:
            formula = formula.replace(char, str(row[char].value))

        for char in formula:
            if char.isdigit():
                result.append(char)
            elif char == "(":
                stack.append(char)
            elif char == ")":
                top = stack.pop()
                while top != "(":
                    result.append(top)
                    top = stack.pop()
            else:
                while (
                    stack
                    and constants.OPERATIONS[stack[-1]] >= constants.OPERATIONS[char]
                ):
                    result.append(stack.pop())
                stack.append(char)

        while len(stack) != 0:
            result.append(stack.pop())

        return result
