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

    for index_i in range(9):
        test = board[8 - index_i][index_i+1:]
        for index_j in range(0, 9-index_i):
            test += board[index_j][index_i]
        for check in range(1, 10):
            if test.count(str(check)) >= 2:
                return False
    return True


def validate_board(board):
    pass