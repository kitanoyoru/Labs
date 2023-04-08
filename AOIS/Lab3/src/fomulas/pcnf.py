import copy

import src.fomulas.constants as constants

from typing import List

from src.table import Table, Row, BoolVar
from src.fomulas.area import Area


class PCNF:
    def __init__(self, table: Table) -> None:
        self._table = table

        self._pcnf = self._generate_pcnf()
        self._minimized_pcnf = self._generate_minimized_pcnf()

        self._calculated_pcnf = self.generate_irredundant_calculated_pcnf()
        self._quine_mcclusky_pcnf = self.generate_irredundant_quine_mcclusky_pcnf()
        self._karnaugh_veitch_pcnf = self.generate_irredundant_karnaugh_veitch_pcnf()

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
        if len(table) == 0:
            return []

        for _ in range(len(table)):
            short_table = self.__start_glued(table)
            table = self.__delete_duplicate_rows(short_table)
            result = table

        result = self.__delete_duplicate_rows(result)

        return result

    def _generate_minimized_pcnf(self) -> str:
        pcnf_table = self._generate_pcnf_table()
        pcnf_short_table = self._generate_short_pcnf_table(pcnf_table)
        minimized_pcnf = self._generate_minimized_pcnf_form(pcnf_short_table)

        return minimized_pcnf

    def _generate_minimized_pcnf_form(self, table: List[Row]) -> str:
        minimized_pcnf = ""

        for row in table:
            if minimized_pcnf != "":
                minimized_pcnf += "&"

            minimized_pcnf += "("
            for char in ["a", "b", "c"]:
                var = row[char]
                if var is not None:
                    minimized_pcnf += f"{char}" if var == 0 else f"!{char}"
                    minimized_pcnf += "|"
            minimized_pcnf = minimized_pcnf[:-1] + ")"

        return minimized_pcnf

    def generate_irredundant_calculated_pcnf(self) -> str:
        #if self.__is_constant_function():
        #    return 0
            
        sign = "&"
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

    def generate_irredundant_quine_mcclusky_pcnf(self) -> str:
        sign = "&"
        short_form = self._minimized_pcnf.split(sign)
        formula = self._pcnf.split(sign)

        if len(short_form) == 1:
            return "".join(short_form)

        terms = []

        for i in short_form:
            if len(i) <= 4:
                terms.append(i)

        table = self.__fill_irredundant_quine_mcclusky_pcnf(formula=formula, short_form=short_form)
        for term1 in formula:
            ones = list(table[term1].values()).count(1)
            if ones == 1:
                for term2 in short_form:
                    if table[term1][term2] == 1 and term2 not in terms:
                        terms.append(term2)

        return sign.join(terms)


    def __fill_irredundant_quine_mcclusky_pcnf(self, formula, short_form) -> str:
        sign = "|"
        table = {}

        for col in formula:
            table[col] = {}

        for col in formula:
            for row in short_form:
                row_terms = row[1:-1].split(sign)
                col_terms = col[1:-1].split(sign)
                if len(row[1:-1]) > 2 and self.__is_row_includes_col(row_terms, col_terms):
                    table[col][row] = 1
                else:
                    table[col][row] = 0

        return table

    
    def generate_irredundant_karnaugh_veitch_pcnf(self) -> str:
        sign, value = "&", 0
        short_form = self._minimized_pcnf.split(sign)

        if len(short_form) == 1:
            return "".join(short_form)

        result, table = [], self._fill_karnaugh_veitch_table()
        
        alg = Area(table=table).check_four_area_line(value).check_square_area(value).check_two_area_line(value).check_one_area(value).minimizing_area()

        areas = [[Row(*data) for data in area] for area in alg.areas]

        for area in areas:
            result.extend(self._generate_short_pcnf_table(area))

        return self._generate_minimized_pcnf_form(result) 

    def _fill_karnaugh_veitch_table(self):
        table = self._generate_pcnf_table()
        dict_table = {row: {} for row in constants.VALUES_A}

        for row in constants.VALUES_A:
            for col in constants.VALUES_B_C:
                if Row(a=row, b=col[0], c=col[1]) in table:
                    dict_table[row][col] = 0
                else:
                    dict_table[row][col] = 1

        return dict_table

    def __is_row_includes_col(self, row, col) -> bool:
        return all(filter(lambda row_term: row_term in col, row))

            
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
                short_table.append(copy.deepcopy(table[i]))

        if len(short_table) == 0:
            return table
        
        return short_table

    def __gluing_rows(self, first: Row, second: Row) -> str:
        false_count: int = 0
        last_false_pos: int = 0

        keys = ["a", "b", "c"]

        for key in keys:
            if first[key] is None and second[key] is None:
                continue
            elif first[key] is None or second[key] is None:
                false_count += 1
                last_false_pos = key
            else:
                is_equal = (first[key] == second[key])
                if not is_equal:
                    false_count += 1
                    last_false_pos = key
        
        if false_count == 1:
            return last_false_pos 

        return -1
