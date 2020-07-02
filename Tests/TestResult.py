from tictactoe import result, X, O, EMPTY

emptyBoard = [[EMPTY, EMPTY, EMPTY],
              [EMPTY, EMPTY, EMPTY],
              [EMPTY, EMPTY, EMPTY]]

Board1 = [[EMPTY, X, EMPTY],
          [EMPTY, EMPTY, EMPTY],
          [EMPTY, EMPTY, EMPTY]]

Board2 = [[EMPTY, X, EMPTY],
          [EMPTY, EMPTY, O],
          [EMPTY, EMPTY, EMPTY]]

if result(emptyBoard, (0, 1)) == Board1:
    print("works")
else:
    print("check failed")

if result(Board1, (1, 2)) == Board2:
    print("works")
else:
    print("check 2 failed")
