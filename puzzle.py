def check_horizontal(board:list[str], row_num: int) -> bool:
    '''
    Check if row is valid to coninue playing
    '''
    for digit in board[row_num]:
        if digit.isdigit() and board[row_num].count(digit) > 1:
            return False
    return True


def check_vertical(board, index):
    stack = []
    for ind, elem in enumerate(board):
        if ind == index and elem.isdigit():
            stack.append(elem)
    for i in stack:
        if stack.count(i) > 1:
            return False
    return True


def check_by_flag(board):
    pass


def validate_board(board):
    pass