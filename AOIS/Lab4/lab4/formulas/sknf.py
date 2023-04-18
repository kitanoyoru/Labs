class SKNF:
    @classmethod
    def create_sknf(cls, table) -> str:
        sknf = ''

        for i in range(len(table)):
            if table[i][3] == 0:
                if sknf:
                    sknf += '*'
                sknf += '(a+' if table[i][0] == 0 else '(!a+'
                sknf += 'b+' if table[i][1] == 0 else '!b+'
                sknf += 'c)' if table[i][2] == 0 else '!c)'

        return sknf


    @classmethod
    def create_sknf_table(cls, table):
        sknf_table = []

        for i in range(len(table)):
            if table[i][3] == 0:
                sknf_table.append([table[i][0], table[i][1], table[i][2]])

        return sknf_table


    @classmethod
    def create_short_sknf_form(cls, table):
        short_form = ""
        elements = {'0': 'a', '1': 'b', '2': 'c'}

        for i in range(len(table)):
            if short_form:
                short_form += '*'
            short_form += '('
            for j in range(len(table[i])):
                if table[i][j] is not None:
                    short_form += elements[str(j)] if table[i][j] == 0 else '!' + elements[str(j)]
                    short_form += '+'
            short_form = short_form.rstrip('+') + ')'

        return short_form