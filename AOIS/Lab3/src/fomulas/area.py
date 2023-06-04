import src.fomulas.constants as constants


class Area:
    table: dict
    areas: list

    def __init__(self, table: dict = None, areas: list = None) -> None:
        if table is None:
            self.table = {}
        else:
            self.table = table

        if areas is None:
            self.areas = []
        else:
            self.areas = areas

    def check_four_area_line(self, value) -> "Area":
        for const in constants.VALUES_A:
            line = [self.table[const][bc] for bc in constants.VALUES_B_C]
            if all(v == value for v in line):
                area = [[const, *constants.VALUES_B_C[j]] for j in range(4)]
                self._add_area(area)

        return self  # For chaining

    def check_square_area(self, value) -> "Area":
        def _first_checker(i, value) -> bool:
            cell1, cell2 = constants.VALUES_B_C[i], constants.VALUES_B_C[i + 1]
            if (
                self.table[0][cell1] == self.table[0][cell2] == value
                and self.table[1][cell1] == self.table[1][cell2] == value
            ):
                return True
            else:
                return False

        def _second_checker(value) -> bool:
            if (
                self.table[0][constants.VALUES_B_C[0]]
                == self.table[0][constants.VALUES_B_C[-1]]
                == value
                and self.table[1][constants.VALUES_B_C[0]]
                == self.table[1][constants.VALUES_B_C[-1]]
                == value
            ):
                return True
            else:
                return False

        areas = [
            [
                [0, *constants.VALUES_B_C[i + 1]],
                [0, *constants.VALUES_B_C[i]],
                [1, *constants.VALUES_B_C[i + 1]],
                [1, *constants.VALUES_B_C[i]],
            ]
            for i in range(len(constants.VALUES_B_C) - 1)
            if _first_checker(i, value)
        ]

        if _second_checker(value):
            areas.append(
                [
                    [0, *constants.VALUES_B_C[0]],
                    [0, *constants.VALUES_B_C[-1]],
                    [1, *constants.VALUES_B_C[0]],
                    [1, *constants.VALUES_B_C[-1]],
                ]
            )

        for area in areas:
            self._add_area(area)

        return self

    def check_one_area(self, value) -> "Area":
        areas = [
            [[const, *constants.VALUES_B_C[i]]]
            for const in constants.VALUES_A
            for i in range(len(constants.VALUES_B_C))
            if self.table[const][constants.VALUES_B_C[i]] == value
        ]

        for area in areas:
            self._add_area(area)

        return self

    def check_two_area_line(self, value) -> "Area":
        areas = (
            [
                [[const, *constants.VALUES_B_C[0]], [const, *constants.VALUES_B_C[-1]]]
                for const in constants.VALUES_A
                if all(self.table[const][col] == value for col in constants.VALUES_B_C)
            ]
            + [
                [
                    [const, *constants.VALUES_B_C[i + 1]],
                    [const, *constants.VALUES_B_C[i]],
                ]
                for const in constants.VALUES_A
                for i in range(len(constants.VALUES_B_C) - 1)
                if self.table[const][constants.VALUES_B_C[i + 1]]
                == self.table[const][constants.VALUES_B_C[i]]
                == value
            ]
            + [
                [
                    [const + 1, *constants.VALUES_B_C[i]],
                    [const, *constants.VALUES_B_C[i]],
                ]
                for const in constants.VALUES_A[:-1]
                for i in range(len(constants.VALUES_B_C))
                if self.table[const + 1][constants.VALUES_B_C[i]]
                == self.table[const][constants.VALUES_B_C[i]]
                == value
            ]
        )

        for area in areas:
            self._add_area(area)

        return self

    def minimizing_area(self) -> "Area":
        new_areas = self.areas.copy()

        for area in self.areas:
            if self.__is_extra_area(area, new_areas):
                self.areas.remove(area)

        self.areas = new_areas

        return self

    def __is_extra_area(self, original_area, areas):
        is_in_count = 0
        for const in original_area:
            for area in areas:
                if const in area and area != original_area:
                    is_in_count += 1
                    break

        return is_in_count != len(original_area)

    def _add_area(self, value):
        if self.__is_in_area(value):
            self.areas.append(value)

    def __is_in_area(self, value) -> bool:
        for area in self.areas:
            is_in = False
            for const in value:
                if const not in area:
                    is_in = True
            if not is_in:
                return False
        return True
