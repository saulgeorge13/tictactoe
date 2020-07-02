from tictactoe import X, O, EMPTY, utility

tie1 = [[O, X, O],
        [O, X, O],
        [X, O, X]]

x1 = [[X, X, X],
      [O, X, O],
      [X, O, X]]

o1 = [[O, O, O],
      [X, X, O],
      [X, O, X]]

if utility(tie1) == 0:
    print("Tie test works")
else:
    print("Tie test failed")

if utility(x1) == 1:
    print("X test works")
else:
    print("X test failed")

if utility(o1) == -1:
    print("O test works")
else:
    print("O test failed")