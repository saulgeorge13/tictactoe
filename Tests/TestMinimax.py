from tictactoe import X, O, EMPTY, terminal, player, result, actions, utility, winner, minimax

board0 = [[EMPTY, EMPTY, EMPTY],
              [EMPTY, EMPTY, EMPTY],
              [EMPTY, EMPTY, EMPTY]]

board1 = [[EMPTY, EMPTY, EMPTY],
              [EMPTY, EMPTY, EMPTY],
              [EMPTY, EMPTY, X]]

board2 = [[O, EMPTY, EMPTY],
          [EMPTY, X, EMPTY],
          [EMPTY, EMPTY, EMPTY]]

move = minimax(board1)
print(move)