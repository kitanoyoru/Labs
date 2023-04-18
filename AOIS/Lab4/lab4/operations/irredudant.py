def is_includes_checking(term_of_short, term_of_base):
    is_includes = True
    for term in term_of_short:
        if term not in term_of_base:
            is_includes = False
    return is_includes


def fill_calculated_tabular_table(formula, short_form, sign):
    sign = '+' if sign == '*' else '*'
    table = dict()
    for col in formula:
        table[col] = dict()
    for col in formula:
        for row in short_form:
            if is_includes_checking(row[1:-1].split(sign), col[1:-1].split(sign)) and len(row[1:-1]) > 2:
                table[col][row] = 1
            else:
                table[col][row] = 0
    return table


def search_uncovered_constituents(table, formula, terms, short_form):
    result, covered_constituents = [], []
    for term in formula:
        for implicate_from_terms in terms:
            if table[term][implicate_from_terms] == 1 and term not in covered_constituents:
                covered_constituents.append(term)
                break
    uncovered_constituents = [term for term in formula if term not in covered_constituents]
    short_form.reverse()
    for term in uncovered_constituents:
        for implicate_from_short in short_form:
            if table[term][implicate_from_short] == 1 and implicate_from_short not in terms:
                result.append(implicate_from_short)
                break
    return result


def irredudant_calculated_tabular(formula, short_form, sing=None):
    short_form = short_form.split(sing)
    formula = formula.split(sing)
    if len(short_form) == 1:
        return ''.join(short_form)
    terms = []
    for i in short_form:
        if len(i) <= 4:
            terms.append(i)
    table = fill_calculated_tabular_table(formula, short_form, sing)
    for term in formula:
        count_of_one = list(table[term].values()).count(1)
        if count_of_one == 1:
            for implicate_from_short in short_form:
                if table[term][implicate_from_short] == 1 and implicate_from_short not in terms:
                    terms.append(implicate_from_short)
    terms.extend(search_uncovered_constituents(table, formula, terms, short_form))
    return sing.join(terms)

