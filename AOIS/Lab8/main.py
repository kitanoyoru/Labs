import math
import random

from lab8 import Memory, MATRIX_SIZE 

random.seed()

def generate_random_int() -> int:
    return random.randint(0, 65535)
    
def pretty_print_matrix(matrix):
    print('\n'.join([' '.join([str(cell) for cell in row]) for row in matrix]))


def main() -> None:
    m = Memory()

    V = [1, 0, 0]

    for i in range(MATRIX_SIZE):
        val = generate_random_int()
        m.write(val, i)

    print("Normal matrix")
    pretty_print_matrix(m.get_normal_matrix())

    print("Diagonal matrix")
    m.to_diagonal_matrix()
    pretty_print_matrix(m.get_normal_matrix())

    print("5th word in matrix")
    print(m.read(5))

    print()

    print("Sum with V (matrix after sum operation)")
    m.sum(V)
    pretty_print_matrix(m.get_normal_matrix())

    print()

    print("Bool func 2 (input - 0, 1; output - 2)")
    m.func_2(0, 1, 2)
    pretty_print_matrix(m.get_normal_matrix())

    print("Bool func 7 (input - 3, 4; output - 5)")
    m.func_7(3, 4, 5)
    pretty_print_matrix(m.get_normal_matrix())

    print("Bool func 8 (input - 6, 7; output - 8)")
    m.func_2(6, 7, 8)
    pretty_print_matrix(m.get_normal_matrix())

    print("Bool func 13 (input - 9, 10; output - 11)")
    m.func_2(9, 10, 11)
    pretty_print_matrix(m.get_normal_matrix())

    print()

    print("Words in range from 7827 to 42355")
    pretty_print_matrix(m.in_range(7827, 42355))


if __name__ == "__main__":
    main()
