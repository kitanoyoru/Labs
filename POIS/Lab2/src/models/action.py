from enum import Enum


class StudentAction(Enum):
    ADD = 1
    DELETE = 2
    FILTER = 3


class DialogAction(Enum):
    OPEN_FILTER_DIALOG = 1
    OPEN_ADD_DIALOG = 2
    OPEN_DELETE_DIALOG = 3
    CLOSE_DIALOG = 4
