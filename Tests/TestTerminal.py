from tictactoe import X, O, EMPTY, terminal

emptyBoard = [[EMPTY, EMPTY, EMPTY],
              [EMPTY, EMPTY, EMPTY],
              [EMPTY, EMPTY, EMPTY]]

tie1 = [[O, X, O],
        [O, X, O],
        [X, O, X]]

x1 = [[X, X, X],
      [O, X, O],
      [X, O, X]]

o1 = [[O, O, O],
      [X, X, O],
      [X, O, X]]

if not terminal(emptyBoard):
    print("Non-terminal check works")
else:
    print("non-terminal check failed")

if terminal(tie1):
    print("Tie test works")
else:
    print("Tie test failed")

if terminal(x1):
    print("X test works")
else:
    print("X test failed")

if terminal(o1):
    print("O test works")
else:
    print("O test failed")