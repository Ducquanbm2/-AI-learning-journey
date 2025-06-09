"""
    TIC TAC TOE
"""


import copy 

X = "X"
O = "O"
EMPTY = None



def initial_state(): 
    table = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    return table


def player(board):
    count = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] != EMPTY:
                count += 1
    if count % 2 == 0:
        return X
    else: return O


def winner(board):
    for i in range(0, 3):
        if board[i][0] != EMPTY:
            if board[i][0] == board[i][1] == board[i][2]: 
                return board[i][0]
    for j in range(0, 3):
        if board[0][j] != EMPTY:
            if board[0][j] == board[1][j] == board[2][j]:
                return board[0][j]
    if board[1][1] != EMPTY:
        if board[0][0] == board[1][1] == board[2][2]:
            return board[1][1]
        if board[0][2] == board[1][1] == board[2][0]:
            return board[1][1]

    return EMPTY


def terminal(board):
    win = winner(board)
    if win != EMPTY:
        return True
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                return False
    return True



def convert(board):
    win = winner(board)
    if win == X: return 1
    elif win == O: return -1
    return 0



def action(board):
    move = []
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                move.append((i, j))
    return move

    


def result(board, move):
    copy_board = copy.deepcopy(board)
    Player = player(board)
    if Player != EMPTY:
        i, j = move
        copy_board[i][j] = Player

    return copy_board



def minimize(board):
    move = action(board)
    copy_board = copy.deepcopy(board)
    ans_value = 1
    if terminal(board) == True:
        return convert(board), None
    ans_move = move[0]
    for i in range(0, len(move)):
        result_board = result(copy_board, move[i])
        cur_value, cur_move = maximize(result_board)
        if ans_value > cur_value:
            ans_value = cur_value
            ans_move = move[i]
    return ans_value, ans_move




def maximize(board):
    move = action(board)
    copy_board = copy.deepcopy(board)
    ans_value = -1
    if terminal(board) == True:
        return convert(board), None
    ans_move = move[0]
    for i in range(0, len(move)):
        result_board = result(copy_board, move[i])
        cur_value, cur_move = minimize(result_board)
        if ans_value < cur_value:
            ans_value = cur_value
            ans_move = move[i]
    return ans_value, ans_move




def minimax(board):
    k = player(board)
    if k == X:
        value, move = maximize(board)
    else:
        value, move = minimize(board)
    return move