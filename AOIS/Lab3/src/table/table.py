import src.table.constants as constants

from dataclasses import dataclass

from typing import Optional, List, Any


@dataclass
class BoolVar:
    value: int


    def __hash__(self) -> int:
        return hash(self.value)

    def __eq__(self, __other: object) -> bool:
        if isinstance(__other, self):
            is_equals = self.value == __other.value
            return is_equals

        raise ValueError()
            
# REFACTOR: maybe rafactor it using __slots__
@dataclass
class Row:
    a: Optional[BoolVar]
    b: Optional[BoolVar]
    c: Optional[BoolVar]

    def __getitem__(self, __key: str) -> BoolVar:
        val = getattr(self, __key)
        return val

    def __eq__(self, __other: object) -> bool:
        if isinstance(__other, self):
            for key in ["a", "b", "c"]:
                if self[key] != __other[key]:
                    return False
            return True

        raise ValueError()

    def __hash__(self) -> int:
        return hash((self.a, self.b, self.c))

    result: Optional[BoolVar] = None


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
            table[i].result = self._get_result(formula, table[i])

    def _get_result(self, formula: str, row: Row) -> BoolVar:
        stack: List[int] = []
        polish = self._polish_notation(formula, row)

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
        print(result)

        return result

    def _polish_notation(self, formula: str, row: Row) -> List[str]:
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
