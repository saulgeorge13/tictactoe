from tictactoe import X, O, EMPTY, winner

empty = [[EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY]]

tie1 = [[O, X, O],
        [O, X, O],
        [X, O, X]]

x1 = [[X, X, X],
      [O, X, O],
      [X, O, X]]

x2 = [[O, O, X],
      [X, X, X],
      [X, O, O]]

x3 = [[O, O, X],
      [X, O, O],
      [X, X, X]]

x4 = [[X, O, X],
      [X, O, X],
      [X, X, O]]

x5 = [[O, X, O],
      [O, X, X],
      [X, X, O]]

x6 = [[O, O, X],
      [X, X, X],
      [O, O, X]]

x7 = [[X, O, O],
      [O, X, X],
      [X, O, X]]

x8 = [[X, O, X],
      [O, X, X],
      [X, O, O]]

o1 = [[O, O, O],
      [EMPTY, X, X],
      [X, O, X]]

o2 = [[X, EMPTY, X],
      [O, O, O],
      [X, O, X]]

o3 = [[X, EMPTY, X],
      [EMPTY, X, X],
      [O, O, O]]

o4 = [[O, X, X],
      [O, X, X],
      [O, EMPTY, O]]

o5 = [[X, O, X],
      [O, O, X],
      [X, O, EMPTY]]

o6 = [[X, EMPTY, O],
      [O, X, O],
      [X, X, O]]

o7 = [[X, O, O],
      [X, O, X],
      [O, EMPTY, X]]

o8 = [[O, O, X],
      [EMPTY, O, X],
      [X, X, O]]


if winner(empty) is None:
    print("Empty check works")
if winner(tie1) is None:
    print("No winner check works")

xTests = [x1, x2, x3, x4, x5, x6, x7, x8]
oTests = [o1, o2, o3, o4, o5, o6, o7, o8]

for i in range(8):
    if winner(xTests[i]) == X:
        print("X", i, "works")
for j in range(8):
    if winner(oTests[j]) == O:
        print("O", j, "works")
