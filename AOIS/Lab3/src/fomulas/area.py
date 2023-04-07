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
            is_line = True
            for j in range(len(constants.VALUES_B_C)):
                if self.table[const][constants.VALUES_B_C[j]] != value:
                    is_line = False
                    break
            area = [[const, *constants.VALUES_B_C[0]], [const, *constants.VALUES_B_C[1]],
                    [const, *constants.VALUES_B_C[2]], [const, *constants.VALUES_B_C[3]]]

            if is_line:
                self._add_area(area)

        return self # For chaining

    def check_square_area(self, value) -> "Area":
        def _first_checker(i,  value) -> bool:
            if self.table[0][constants.VALUES_B_C[i + 1]] == self.table[0][constants.VALUES_B_C[i]] == value\
                and self.table[1][constants.VALUES_B_C[i + 1]] == self.table[1][constants.VALUES_B_C[i]] == value:
                return True
            return False
        
        def _second_checker(value) -> bool:
            if self.table[0][constants.VALUES_B_C[0]] == self.table[0][constants.VALUES_B_C[-1]] == value \
                    and self.table[1][constants.VALUES_B_C[0]] == self.table[1][constants.VALUES_B_C[-1]] == value:
                    return True
            return False

        for i in range(len(constants.VALUES_B_C)):
            if i + 1 < len(constants.VALUES_B_C):
                if _first_checker(i, value):
                    area = [[0, *constants.VALUES_B_C[i+1]], [0, *constants.VALUES_B_C[i]], [1, *constants.VALUES_B_C[i+1]], [1, *constants.VALUES_B_C[i]]]
                    self._add_area(area)

            
        if _second_checker(value):
            area = [[0, *constants.VALUES_B_C[0]], [0, *constants.VALUES_B_C[-1]], [1, *constants.VALUES_B_C[0]], [1, *constants.VALUES_B_C[-1]]]
            self._add_area(area)

        return self

    def check_one_area(self, value) -> "Area":
        for const in constants.VALUES_A:
            for i in range(len(constants.VALUES_B_C)):
                if self.table[const][constants.VALUES_B_C[i]] == value:
                    area = [[const, *constants.VALUES_B_C[i]]]
                    self._add_area(area)

        return self

    def check_two_area_line(self, value) -> "Area":
        for const in constants.VALUES_A:
            for i in range(len(constants.VALUES_B_C)):
                if self.table[const][constants.VALUES_B_C[0]] == self.table[const][constants.VALUES_B_C[-1]] == value:
                    area = [[const, *constants.VALUES_B_C[0]], [const, *constants.VALUES_B_C[-1]]]
                    self._add_area(area)

                if i + 1 < len(constants.VALUES_B_C):
                    if self.table[const][constants.VALUES_B_C[i + 1]] == self.table[const][constants.VALUES_B_C[i]] == value:
                        area = [[const, *constants.VALUES_B_C[i + 1]], [const, *constants.VALUES_B_C[i]]]
                        self._add_area(area)

                if const + 1 < 2:
                    if self.table[const+ 1][constants.VALUES_B_C[i]] == self.table[const][constants.VALUES_B_C[i]] == value:
                        area = [[const + 1, *constants.VALUES_B_C[i]], [const, *constants.VALUES_B_C[i]]]
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