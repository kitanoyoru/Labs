from typing import Callable

from functools import partial


class DNF:
    def __init__(self, formula: str, checkers: Callable[[str], bool]) -> None:
        self._checkers = [partial(checker, formula) for checker in checkers]

    def validate(self) -> bool:
        return all(checker() for checker in self._checkers)

    