import copy

import src.fomulas.constants as constants

from typing import List

from src.table import Table, Row, BoolVar
from src.fomulas.area import Area


class PDNF:
    def __init__(self, table: Table) -> None:
        self._table = table

        self._sign = "|"

        self._pdnf = self._generate_pdnf()
        self._minimized_pdnf = self._generate_minimized_pdnf()

        self._calculated_pdnf = self.generate_irredundant_calculated_pdnf()
        self._quine_mcclusky_pdnf = self.generate_irredundant_quine_mcclusky_pdnf()
        self._karnaugh_veitch_pdnf = self.generate_irredundant_karnaugh_veitch_pdnf()

    def generate_irredundant_calculated_pdnf(self) -> str:
        short_form = self._minimized_pdnf

        pdnf_table = self._generate_pdnf_table()
        short_table = self._generate_short_pdnf_table(pdnf_table)

        terms = short_form.split(self._sign)
        if len(terms) <= 2:
            return self._sign.join(terms)

        for i, term in enumerate(short_table):
            formula = self._sign.join([t for j, t in enumerate(terms) if j != i])
            if self.__is_important_term(formula, term):
                terms[i] = ""

        return self._sign.join([t for t in terms if t != ""])

    def generate_irredundant_quine_mcclusky_pdnf(self) -> str:
        short_form = self._minimized_pdnf.split(self._sign)
        formula = self._pdnf.split(self._sign)

        if len(short_form) == 1:
            return "".join(short_form)

        terms = [i for i in short_form if len(i) <= 4]

        table = self.__fill_irredundant_quine_mcclusky_pdnf(
            formula=formula, short_form=short_form
        )
        ones = [[term1, list(table[term1].values()).count(1)] for term1 in formula]

        for term1, ones_count in ones:
            if ones_count == 1:
                terms += [
                    term2
                    for term2 in short_form
                    if table[term1][term2] == 1 and term2 not in terms
                ]

        return self._sign.join(terms)

    def generate_irredundant_karnaugh_veitch_pdnf(self) -> str:
        value = 1

        short_form = self._minimized_pdnf.split(self._sign)

        if len(short_form) == 1:
            return "".join(short_form)

        result, table = [], self._fill_karnaugh_veitch_table()

        alg = (
            Area(table=table)
            .check_four_area_line(value)
            .check_square_area(value)
            .check_two_area_line(value)
            .check_one_area(value)
            .minimizing_area()
        )

        areas = [[Row(*data) for data in area] for area in alg.areas]

        for area in areas:
            result.extend(self._generate_short_pdnf_table(area))

        return self._generate_minimized_pdnf_form(result)

    def _generate_pdnf(self) -> str:
        pdnf_terms = []
        for row in self._table:
            if row.result == BoolVar(1):
                term = "&".join(
                    [
                        char if row[char].value == 1 else f"!{char}"
                        for char in ["a", "b", "c"]
                    ]
                )
                pdnf_terms.append(f"({term})")

        return "|".join(pdnf_terms)

    def _generate_pdnf_table(self) -> List[Row]:
        pdnf_table: List[Row] = list(
            filter(lambda row: row.result.value == 1, self._table)
        )
        return pdnf_table

    def _generate_short_pdnf_table(self, table: List[Row]) -> List[Row]:
        short_table = self.__start_glued(table)
        while True:
            new_table = self.__delete_duplicate_rows(short_table)
            if len(new_table) == len(short_table):
                break
            short_table = new_table

        return short_table

    def _generate_minimized_pdnf(self) -> str:
        pdnf_table = self._generate_pdnf_table()
        pdnf_short_table = self._generate_short_pdnf_table(pdnf_table)
        minimized_pdnf = self._generate_minimized_pdnf_form(pdnf_short_table)

        return minimized_pdnf

    def _generate_minimized_pdnf_form(self, table: List[Row]) -> str:
        pdnf_terms = []
        for row in table:
            term = []
            for char in ["a", "b", "c"]:
                var = row[char]
                if var is not None:
                    term.append(char if var == 1 else f"!{char}")
            if term:
                pdnf_terms.append("&".join(term))

        return self._sign.join([f"({term})" for term in pdnf_terms])

    def __fill_irredundant_quine_mcclusky_pdnf(self, formula, short_form):
        sign = "&"
        table = {}

        table = {
            col: {
                row: 1
                if len(row[1:-1]) > 2
                and self.__is_row_includes_col(
                    row[1:-1].split(sign), col[1:-1].split(sign)
                )
                else 0
                for row in short_form
            }
            for col, col_terms in zip(
                formula, map(lambda x: x[1:-1].split(sign), formula)
            )
        }

        return table

    def _fill_karnaugh_veitch_table(self):
        table = self._generate_pdnf_table()
        dict_table = {
            row: {
                col: 1 if Row(a=row, b=col[0], c=col[1]) in table else 0
                for col in constants.VALUES_B_C
            }
            for row in constants.VALUES_A
        }

        return dict_table

    def __is_row_includes_col(self, row, col) -> bool:
        return all(map(lambda row_term: row_term in col, row))

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

    def __gluing_rows(self, first: Row, second: Row):
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
                is_equal = first[key] == second[key]
                if not is_equal:
                    false_count += 1
                    last_false_pos = key

        if false_count == 1:
            return last_false_pos

        return -1
