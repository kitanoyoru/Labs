def get_minimized(table, callback):
    short_logic_table = create_short_logic_table(table)
    return callback(short_logic_table)


def create_short_logic_table(table) -> list:
    if len(table) == 0:
        return []

    result = []

    for i in range(len(table[0])):
        short_logic_table = start_glued(table)
        table = delete_duplicate(short_logic_table)
        result = table
        
    return delete_duplicate(result)


def start_glued(table):
    short_logic_table = []
    index = []

    for i in range(len(table)):
        is_not_gluing = False
        for j in range(i+1, len(table)):
            false_index = gluing_of_vectors(table[i], table[j])
            if false_index >= 0:
                is_not_gluing = True
                index.append(j)
                new_vector = table[i].copy()
                new_vector[false_index] = None
                short_logic_table.append(new_vector)
        if not is_not_gluing and i not in index:
            short_logic_table.append(table[i])
            
    if short_logic_table is not None:
        return short_logic_table

    return table


def delete_duplicate(table):
    new_table = []

    for vector in table:
        if vector not in new_table:
            new_table.append(vector)

    return new_table


def gluing_of_vectors(first_vector, second_vector):
    result_vector = []

    for i in range(len(first_vector)):
         result_vector.append(first_vector[i] == second_vector[i])
    if result_vector.count(False) == 1:
        return result_vector.index(False)

    return -1