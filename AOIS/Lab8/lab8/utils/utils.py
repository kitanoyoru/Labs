from typing import List


def convert_to_bytes(x: int) -> List[int]:
    rev_bytes: List[int] = []

    while x != 0:
        rev_bytes.append(x % 2)
        x //= 2

    while len(rev_bytes) != 8:
        rev_bytes.append(0)

    return rev_bytes[::-1]
