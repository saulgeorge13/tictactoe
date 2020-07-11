"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


# returns starting state of the board
def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


# returns player with next turn, returns O if board is full
def player(board):
    x = 0
    o = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x = x + 1
            elif board[i][j] == O:
                o = o + 1
    if x == o:
        return X
    else:
        return O


# returns the set of all possible action (i, j) available on the board
def actions(board):
    possibleMoves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possibleMoves.add((i, j))
    return possibleMoves


# returns the board that results from making move (i, j) on the board
def result(board, action):
    if action[0] < 3 and action[1] < 3 and board[action[0]][action[1]] is EMPTY:
        newBoard = copy.deepcopy(board)
        newBoard[action[0]][action[1]] = player(board)
        return newBoard
    else:
        raise Exception("Invalid action exception")


# returns the winner of the game if there is one
def winner(board):
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
    return None


# returns true if the game is over and false otherwise
def terminal(board):
    empty_counter = 0
    if winner(board) is not None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    else:
        return True


# returns 1 if X has won, -1 if O has won, 0 otherwise
def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


# returns the optimal move for the player on a board
def minimax(board):
    if terminal(board):
        return None

    if player(board) == X:
        bestScore = -math.inf
        if empty(board):
            return (0, 0)
        for action in actions(board):
            moveScore = minval(result(board, action))
            if moveScore > bestScore:
                bestScore = moveScore
                bestMove = action
        return bestMove
    else:
        bestScore = math.inf
        for action in actions(board):
            moveScore = maxval(result(board, action))
            if moveScore < bestScore:
                bestScore = moveScore
                bestMove = action
        return bestMove


def minval(board):
    if terminal(board):
        return utility(board)
    score = math.inf
    for action in actions(board):
        score = min(score, maxval(result(board, action)))
        if score == -1:
            break
    return score


def maxval(board):
    if terminal(board):
        return utility(board)
    score = -math.inf
    for action in actions(board):
        score = max(score, minval(result(board, action)))
        if score == 1:
            break
    return score


# checks if board is empty
def empty(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == X or board[i][j] == O:
                return False
    return True
