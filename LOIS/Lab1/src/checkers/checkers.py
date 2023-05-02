from typing import List

from src.checkers.constants import ENG_ALPH, ALLOWED_CHARS


def check_for_empty(formula: str) -> bool:
    return not formula 

def check_for_space(formula: str) -> bool:
    return " " in formula

def check_for_allowed_chars(formula: str) -> bool:
    def closure(ch: str) -> bool:
        return ch in ENG_ALPH or ch in ALLOWED_CHARS

    return all(map(lambda ch: closure(ch), formula.split()))

def check_for_correct_brackets(formula: str) -> bool:
    stack: List[str] = []
    for ch in formula:
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            if len(stack) or stack[-1] == "(":
                return False

            stack.pop()
            
    return not stack

def check_negation(formula: str) -> bool:
    invalid_operators = set("&|()")

    for pos in range(len(formula) - 1):
        if formula[pos] == "!" and formula[pos+1] in invalid_operators:
            return False

    return True

def check_disjunction(formula: str) -> bool:
    is_open = False

    for ch in formula:
        if ch == "(":
            is_open = True
        if ch == ")":
            is_open = False

        if ch == "|" and is_open:
            return False
        
    return True











