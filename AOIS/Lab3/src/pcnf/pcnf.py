import copy

from typing import List

from src.table import Table, Row
from src.table.constants import TABLE_ROWS


class PCNF:
    def __init__(self, table: Table) -> None:
        self._table = table

        self._pcnf = self._generate_pcnf()
        self._minimized_pcnf = self._generate_minimized_pcnf()

        self._calculated_pcnf = self._generate_irredundant_calculated_pcnf()
        self._quine_mcclusky_pcnf = self._generate_irredundant_quine_mcclusky_pcnf()
        self._karnaugh_veitch_pcnf = self._generate_irredundant_karnaugh_veitch_pcnf()

    def _generate_pcnf(self) -> str:
        pcnf = ""

        for row in self._table:
            if pcnf != "":
                pcnf += "&"

            pcnf += "("
            for char in ["a", "b", "c"]:
                pcnf += f"{char}|" if row[char].value == 0 else f"!{char}|"
            pcnf[-1] = ")"

        return pcnf

    def _generate_pcnf_table(self) -> List[Row]:
        pcnf_table: List[Row] = list(
            filter(lambda row: row.result.value == 0, self._table)
        )
        return pcnf_table
    
    def _generate_short_pcnf_table(self, table: List[Row]) -> List[Row]:
        result = []
        if not len(table):
            return []

        for _ in range(3):
            short_table = self.__start_glued(table)
            table = self.__delete_duplicate_rows(short_table)
            result = table

        result = self.__delete_duplicate_rows(result)

        return result

    def _generate_minimized_pcnf(self) -> str:
        pcnf_table = self._generate_pcnf_table()
        pcnf_short_table = self._generate_short_pcnf_table(pcnf_table)

        minimized_pcnf = ""

        for row in pcnf_short_table:
            if minimized_pcnf != "":
                minimized_pcnf += "&"

            minimized_pcnf += "("
            for char in ["a", "b", "c"]:
                var = row[char]
                if var is not None:
                    minimized_pcnf += f"{char}" if var.value == 0 else f"!{char}"
                    minimized_pcnf += "|"
            minimized_pcnf[-1] = ")"

        return minimized_pcnf

    def __delete_duplicate_rows(self, table: List[Row]) -> List[Row]:
        return list(set(table))

    def __start_glued(self, table: List[Row]) -> List[Row]:
        short_table: List[Row] = []
        visited_idx: List[int] = []

        for i in range(TABLE_ROWS):
            is_glued = False
            for j in range(i + 1, TABLE_ROWS):
                idx = self.__gluing_rows(table[i], table[j])
                if idx != -1:
                    is_glued = True
                    visited_idx.append(j)

                    new_row = copy.deepcopy(table[i])
                    new_row[idx] = None 

                    short_table.append(new_row)

            if not is_glued and i not in visited_idx:
                short_table.append(table[i])

        if len(short_table) == 0:
            return table
        
        return short_table

    def __gluing_rows(first: Row, second: Row) -> str:
        false_count: int = 0
        last_false_pos: int = 0

        for key in ["a", "b", "c"]:
            is_equal = (first[key].value == second[key].value)
            if not is_equal:
                false_count += 1
                last_false_pos = key
        
        if false_count == 1:
            return last_false_pos 

        return -1
