from typing import List


MAX_BYTES = 8

def convert_to_bytes(x: int) -> List[int]:
    rev_bytes: List[int] = []

    while x != 0:
        rev_bytes.append(x % 2)
        x //= 2

    while len(rev_bytes) != MAX_BYTES:
        rev_bytes.append(0)

    return rev_bytes[::-1]
