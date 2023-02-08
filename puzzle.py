def check_horizontal(board: list, row_num: int) -> bool:
    """
    Function checks if there are no same digit numbers
    in one row on the board.
    """
    for digit in board[row_num]:
        if digit.isdigit() and board[row_num].count(digit) > 1:
            return False
    return True


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
    for index_i in range(9):
        test = board[8 - index_i][index_i+1:]
        for index_j in range(0, 9-index_i):
            test += board[index_j][index_i]
        for check in range(1, 10):
            if test.count(str(check)) >= 2:
                return False
    return True


def validate_board(board):
    """
    Validates all the board
    """
    for i in range(9):
        if not (check_horizontal(board, i) and check_vertical(board, i)):
            return False
    if not check_by_flag(board):
        return False
    return True