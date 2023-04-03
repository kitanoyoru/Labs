import copy

from typing import List

from src.table import Table, Row, BoolVar
from src.table.constants import TABLE_ROWS


class PCNF:
    def __init__(self, table: Table) -> None:
        self._table = table

        self._pcnf = self._generate_pcnf()
        self._minimized_pcnf = self._generate_minimized_pcnf()

        self._calculated_pcnf = self.generate_irredundant_calculated_pcnf()
        #self._quine_mcclusky_pcnf = self._generate_irredundant_quine_mcclusky_pcnf()
        #self._karnaugh_veitch_pcnf = self._generate_irredundant_karnaugh_veitch_pcnf()

    def _generate_pcnf(self) -> str:
        pcnf = ""

        for row in self._table:
            if row.result  == BoolVar(0):
                if pcnf != "":
                    pcnf += "&"

                pcnf += "("
                for char in ["a", "b", "c"]:
                    pcnf += f"{char}|" if row[char].value == 0 else f"!{char}|"
                pcnf = pcnf[:-1] + ")"

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
            minimized_pcnf = minimized_pcnf[:-1] + ")"

        return minimized_pcnf

    def generate_irredundant_calculated_pcnf(self) -> str:
        #if self.__is_constant_function():
        #    return 0
            
        sign = "|"
        short_form = self._minimized_pcnf

        pcnf_table = self._generate_pcnf_table()
        short_table = self._generate_short_pcnf_table(pcnf_table)

        terms = short_form.split(sign)
        if len(terms) <= 2:
            return sign.join(terms)

        for i in range(len(short_table)):
            formula = short_form.split(sign)
            formula.pop(i)
            formula = sign.join(formula)
            if self.__is_important_term(formula, short_table[i]):
                terms[i] = ""

        joined_terms = sign.join(terms).strip(sign)
            
        return joined_terms
            
    def __is_constant_function(self) -> bool:
        return len(list(filter(lambda row: row.result != BoolVar(0), self._table))) > 0

    def __is_important_term(self, formula: str, row: Row) -> bool:
        if not row.has_none_field:
            return False

        none_field = ""
        for char in ["a", "b", "c"]:
            if row[char] is None:
                none_field = char
                break
        
        row_with_zero, row_with_one = copy.deepcopy(row), copy.deepcopy(row)
        row_with_one[none_field] = 1
        row_with_zero[none_field] = 0

        res_with_one = Table._get_result(formula, row_with_one)
        res_with_zero = Table._get_result(formula, row_with_zero)

        return res_with_one == res_with_zero
        
    def __delete_duplicate_rows(self, table: List[Row]) -> List[Row]:
        return list(set(table))

    def __start_glued(self, table: List[Row]) -> List[Row]:
        short_table: List[Row] = []
        visited_idx: List[int] = []

        for i in range(len(table)):
            is_glued = False
            for j in range(i + 1, len(table)):
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

    def __gluing_rows(self, first: Row, second: Row) -> str:
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
