position = tuple[int, int]


def position_create(row: int, col: int) -> position:

    if not (type(row) is int and row >= 0) or not(type(col) is int and col >= 0):
        raise ValueError('position_create: invalid arguments')
    return row, col


def position_is(pos: position) -> bool:
    return type(pos) is tuple


def position_row(pos: position) -> int:
    if not position_is(pos):
        raise ValueError('position_row: invalid arguments')
    return pos[0]


def position_col(pos: position) ->int:
    if not position_is(pos):
        raise ValueError('position_col: invalid arguments')
    return pos[1]


def position_equal(pos1: position, pos2: position) -> bool:
    if not position_is(pos1) or not position_is(pos2):
        raise ValueError('position_equal: invalid arguments')
    return pos1 == pos2


def position_str(pos: position) -> str:
    if not position_is(pos):
        raise ValueError('position_str: invalid arguments')
    str1 = ', '
    str2 = str1.join([str(p) for p in pos])
    return '(' + str2 + ')'