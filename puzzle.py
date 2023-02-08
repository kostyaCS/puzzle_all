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
    >>> check_vertical(['111***', '1****'], 0)
    False
    """
    stack = []
    for ind, elem in enumerate(board):
        for j in range(len(elem)):
            if j == index and elem[j].isdigit():
                stack.append(j)
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


def validate_board(board):

    for i in range(9):
        if not (check_horizontal(board, i) and check_vertical(board, i)):
            return False

    return check_by_flag(board)
