from tictactoe import EMPTY, actions, X, O

emptyBoard = [[EMPTY, EMPTY, EMPTY],
              [EMPTY, EMPTY, EMPTY],
              [EMPTY, EMPTY, EMPTY]]
action1 = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
if actions(emptyBoard) == action1:
    print("emptyBoard actions work")
else:
    print("emptyBoard check failed")

Board1 = [[EMPTY, X, EMPTY],
          [EMPTY, EMPTY, EMPTY],
          [EMPTY, EMPTY, EMPTY]]
action2 = [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
if actions(Board1) == action2:
    print("1move actions work")
else:
    print("1move check failed")

Board2 = [[EMPTY, X, EMPTY],
          [EMPTY, EMPTY, O],
          [EMPTY, EMPTY, EMPTY]]
action3 = [(0, 0), (0, 2), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2)]
if actions(Board2) == action3:
    print("2move actions work")
else:
    print("2move check failed")

fullBoard = [[X, X, X],
             [X, X, O],
             [X, X, X]]
action4 = []
if actions(fullBoard) == action4:
    print("fullBoard actions work")
else:
    print("fullBoard check failed")
