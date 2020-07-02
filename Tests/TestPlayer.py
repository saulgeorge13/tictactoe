from tictactoe import EMPTY, X, player, O

emptyBoard = [[EMPTY, EMPTY, EMPTY],
              [EMPTY, EMPTY, EMPTY],
              [EMPTY, EMPTY, EMPTY]]
if player(emptyBoard) == X:
    print("empty board works")
else:
    print("check failed")

oneX = [[EMPTY, EMPTY, EMPTY],
              [EMPTY, X, EMPTY],
              [EMPTY, EMPTY, EMPTY]]
if player(oneX) == X:
    print("check failed")
else:
    print("oneX check works")

oneRound = [[EMPTY, EMPTY, O],
              [EMPTY, X, EMPTY],
              [EMPTY, EMPTY, EMPTY]]
if player(emptyBoard) == X:
    print("oneRound check works")
else:
    print("check failed")




