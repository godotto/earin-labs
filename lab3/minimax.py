import numpy as np


def heuristic_function(state):
    crosses = ['x', 'x', 'x']
    noughts = ['o', 'o', 'o']

    for i in range(3):
        if (
            np.array_equal(crosses, board[:, i])
            or np.array_equal(crosses, board[i])
            or np.array_equal(crosses, board.diagonal())
            or np.array_equal(crosses, np.fliplr(board).diagonal())
        ):
            return 1
        elif (
            np.array_equal(noughts, board[:, i])
            or np.array_equal(noughts, board[i])
            or np.array_equal(noughts, board.diagonal())
            or np.array_equal(noughts, np.fliplr(board).diagonal())
        ):
            return -1

    if ' ' not in state:
        return 0
