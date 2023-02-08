def check_horizontal(board, row_num):
    pass


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

    for i in range(9):
        if not (check_horizontal(board, i) and check_vertical(board, i)):
            return False

    return check_by_flag(board)
