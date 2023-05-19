from typing import List

from lab8.constants import MATRIX_SIZE

def convert_to_bytes(x: int) -> List[int]:
    rev_bytes: List[int] = []

    while x != 0:
        rev_bytes.append(x % 2)
        x //= 2

    while len(rev_bytes) != MATRIX_SIZE:
        rev_bytes.append(0)

    return rev_bytes[::-1]


def sum_two_bin(a: List[int], b: List[int]) -> List[int]:
    ans: List[int] = []

    carry = 0

    for i in range(3, -1, -1):
        match a[i] + b[i] + carry:
            case 1:
                ans.insert(0, 1)
                carry = 0
            case 2:
                ans.insert(0, 0)
                carry = 1
            case 3:
                ans.insert(0, 1)
            case _:
                ans.insert(0, 0)

    ans.insert(0, carry)

    return ans
