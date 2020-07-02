"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


# if terminal returns O
def player(board):
    x = 0
    o = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x = x + 1
            elif board[i][j] == O:
                o = o + 1
    if x == 0 or x == o:
        return X
    else:
        return O


def actions(board):
    possibleMoves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possibleMoves.append((i, j))
    return possibleMoves


# invalid action exception required
def result(board, action):
    newBoard = board
    newBoard[action[0]][action[1]] = player(board)
    return newBoard


def winner(board):
    winCheck = [0, 0, 0, 0, 0, 0, 0, 0]
    # each element in the list handles one possible way of winning, row 1-3, column 1-3, diag 1 and 2
    if board[0][0] == X and board[1][0] == X and board[2][0] == X:
        return X
    elif board[0][1] == X and board[1][1] == X and board[2][1] == X:
        return X
    elif board[0][2] == X and board[1][2] == X and board[2][2] == X:
        return X
    elif board[0][0] == X and board[0][1] == X and board[0][2] == X:
        return X
    elif board[1][0] == X and board[1][1] == X and board[1][2] == X:
        return X
    elif board[2][0] == X and board[2][1] == X and board[2][2] == X:
        return X
    elif board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    elif board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X
    elif board[0][0] == O and board[1][0] == O and board[2][0] == O:
        return O
    elif board[0][1] == O and board[1][1] == O and board[2][1] == O:
        return O
    elif board[0][2] == O and board[1][2] == O and board[2][2] == O:
        return O
    elif board[0][0] == O and board[0][1] == O and board[0][2] == O:
        return O
    elif board[1][0] == O and board[1][1] == O and board[1][2] == O:
        return O
    elif board[2][0] == O and board[2][1] == O and board[2][2] == O:
        return O
    elif board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    elif board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O


def terminal(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    if winner(board) is not None:
        return True
    else:
        return False


def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    if terminal(board):
        return None
