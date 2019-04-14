import numpy as np

BOARD_3x3 = [np.array([[0, 3, 0],
                       [3, 0, 2],
                       [0, 2, 0]]),
             np.array([[0, 4, 3],
                       [0, 0, 2],
                       [3, 4, 0]]),
             np.array([[0, 0, 0],
                       [5, 0, 3],
                       [0, 0, 0]])]

BOARD_4x4 = [np.array([[0, 0, 4, 0],
                       [3, 0, 0, 0],
                       [0, 0, 0, 2],
                       [0, 7, 0, 0]]),
             np.array([[2, 0, 0, 0],
                       [0, 0, 3, 0],
                       [0, 5, 0, 0],
                       [0, 0, 0, 6]]),
             np.array([[0, 0, 5, 0],
                       [0, 0, 0, 2],
                       [5, 0, 0, 0],
                       [0, 5, 0, 0]])]

BOARD_5x4 = [np.array([[4, 0, 5, 0, 0],
                       [6, 0, 0, 0, 0],
                       [0, 0, 0, 0, 7],
                       [0, 0, 0, 0, 5]]),
             np.array([[0, 0, 0, 0, 4],
                       [0, 7, 8, 0, 0],
                       [0, 0, 7, 6, 0],
                       [5, 0, 0, 0, 0]]),
             np.array([[0, 6, 0, 0, 0],
                       [0, 6, 7, 0, 0],
                       [0, 0, 4, 5, 0],
                       [0, 0, 0, 5, 0]])]

BOARD_5x5 = [np.array([[0, 3, 0, 0, 0],
                       [0, 0, 0, 0, 4],
                       [0, 0, 9, 0, 0],
                       [3, 0, 0, 0, 0],
                       [0, 0, 0, 8, 0]]),
             np.array([[0, 8, 0, 8, 0],
                       [0, 5, 0, 0, 0],
                       [0, 8, 0, 8, 0],
                       [0, 0, 0, 9, 0],
                       [0, 6, 0, 6, 0]]),
             np.array([[0, 0, 0, 6, 0],
                       [0, 0, 0, 8, 7],
                       [0, 0, 0, 0, 0],
                       [4, 6, 0, 0, 0],
                       [0, 8, 0, 0, 0]])]

BOARDS = [BOARD_3x3, BOARD_4x4, BOARD_5x4, BOARD_5x5]