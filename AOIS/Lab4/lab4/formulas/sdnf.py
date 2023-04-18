class SDNF:
    @classmethod
    def create_sdnf(cls, table) -> str:
        sdnf = ''

        for i in range(len(table)):
            if table[i][4] == 1:
                if sdnf:
                    sdnf += '+'
                sdnf += '(!a*' if table[i][0] == 0 else '(a*'
                sdnf += '!b*' if table[i][1] == 0 else 'b*'
                sdnf += '!c*' if table[i][2] == 0 else 'c*'
                sdnf += '!d)' if table[i][3] == 0 else 'd)'

        return sdnf

    @classmethod
    def create_sdnf_table(cls, table):
        sdnf_table = []

        for i in range(len(table)):
            if table[i][4] == 1:
                sdnf_table.append([table[i][0], table[i][1], table[i][2], table[i][3]])

        return sdnf_table

    @classmethod
    def create_short_sdnf_form(cls, table):
        short_form = ""
        elements = {'0': 'a', '1': 'b', '2': 'c', '3': 'd'}

        for i in range(len(table)):
            if short_form:
                short_form += '+'
            short_form += '('
            for j in range(len(table[i])):
                if table[i][j] is not None:
                    short_form += '!' + elements[str(j)] if table[i][j] == 0 else elements[str(j)]
                    short_form += '*'
            short_form = short_form.rstrip('*') + ')'

        return short_form