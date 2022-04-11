import numpy as np


def heuristic_function(board):
    # lists for comparison
    crosses = ['x', 'x', 'x']
    noughts = ['o', 'o', 'o']

    for i in range(3):
        if ( # crosses win
            np.array_equal(crosses, board[:, i])
            or np.array_equal(crosses, board[i])
            or np.array_equal(crosses, board.diagonal())
            or np.array_equal(crosses, np.fliplr(board).diagonal())
        ):
            return 1
        elif ( # noughts win
            np.array_equal(noughts, board[:, i])
            or np.array_equal(noughts, board[i])
            or np.array_equal(noughts, board.diagonal())
            or np.array_equal(noughts, np.fliplr(board).diagonal())
        ):
            return -1

    # draw
    if ' ' not in board:
        return 0

def minimax(board, alpha, beta, is_maximizing):
    heuristic_value = heuristic_function(board)
    if heuristic_value is not None:
        return heuristic_value, None

    optimal_field = None

    if is_maximizing:
        value = np.NINF

        # check different combinations of putting a cross
        for i in range(9):
            if board.flat[i] == ' ':
                board.flat[i] = 'x'
                prev_value = value
                value = max(value, minimax(board, alpha, beta, False)[0])
                board.flat[i] = ' '

                alpha = max(alpha, value)
                optimal_field = i if value > prev_value else optimal_field

                if value >= beta:
                    break

        return value, optimal_field
    else:
        value = np.inf

        # check different combinations of putting a nought
        for i in range(9):
            if board.flat[i] == ' ':
                board.flat[i] = 'o'
                prev_value = value
                value = min(value, minimax(board, alpha, beta, True)[0])
                board.flat[i] = ' '

                beta = min(beta, value)
                optimal_field = i if value < prev_value else optimal_field

                if value <= alpha:
                    break

        return value, optimal_field
