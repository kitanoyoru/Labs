TABLE_ROWS = 8
INIT_TABLE_DATA = [
    [0, 0, 0],
    [0, 0, 1],
    [0, 1, 0],
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 1],
]

OPERATIONS = {
    "!": 4,
    "&": 3,
    "|": 2,
    "(": 1,
}

OPERATION_HANDLERS = {
    "!": lambda x: 0 if int(x) else 1,
    "&": lambda a, b: 1 if int(a) and int(b) else 0,
    "|": lambda a, b: 1 if int(a) or int(b) else 0,
}
