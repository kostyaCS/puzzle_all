def check_horizontal(board: list, row_num: int) -> bool:
    """
    Function checks if there are no same digit numbers
    in one row on the board.
    """
    pass


def check_vertical(board: list, index: int) -> bool:
    """
    Function checks if there are no same digit numbers
    in one column on the board.
    """
    stack = []
    for ind, elem in enumerate(board):
        if ind == index and elem.isdigit():
            stack.append(elem)
    for i in stack:
        if stack.count(i) > 1:
            return False
    return True


def check_by_flag(board: list) -> bool:
    """
    Function checks if there are no same digit numbers
    in one flag on the board.
    """
    pass
