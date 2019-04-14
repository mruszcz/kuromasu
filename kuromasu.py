import time

import numpy as np

import utils


class Kuromasu:
    """Class storing board of Kuromasu game,
    has methods for solving given board using A* or DF algorithms.

    Initialize object with board, note that max size is 5x5
    due to recursion limit
    """

    def __init__(self, board):
        self.board = board
        self.solvedBoard = {"board": np.empty_like(self.board),
                            "length": np.inf}
        self.executionTime = 0
        self.iterations = 0
        self.foundSolution = False

    def solve(self, mode):
        """Method for solvind the board
        Arguments: self, mode
        mode can be either A* or DF"""

        if mode == "Astar":
            # A* algortihm
            self._astar()

        elif mode == "DF":
            # depth-first algorithm
            self._DF()

        else:
            print("Argument error! Wrong argument for solve method")

    def print(self):
        print("Starting board:\n", self.board,
              "\nSolved board:\n", self.solvedBoard["board"],
              "\nExecution time: {}, Iteration count: {}".format(
                  self.executionTime,
                  self.iterations))

    def _isShorter(self, board):
        return utils.length(board) < self.solvedBoard["length"]

    def _initialize(self):
        for i in range(len(self.board)):
            row = self.board[i]
            for j in range(0, len(row)):
                if row[j] == 0:
                    self.board[i][j] = 1

    def _DF(self):
        """Implementation of depth-first algorithm"""

        self._initialize()  # whiten all

        entryTime = time.process_time()
        self.iterations = 0

        self._recursiveDF(self.board, self.board)

        exitTime = time.process_time()
        self.executionTime = exitTime - entryTime

    def _recursiveDF(self, prvBoard, currBoard):
        """Method finding shortest solution to the puzzle,
            using recursive strategy"""

        self.iterations += 1

        if utils.validate(currBoard):
            if utils.isSolution(currBoard) and self._isShorter(currBoard):
                self.solvedBoard["board"] = currBoard
                self.solvedBoard["length"] = utils.length(currBoard)

            nextBoard = utils.placeNextBlack(currBoard=currBoard,
                                             prvBoard=prvBoard)
            if not np.array_equal(nextBoard, prvBoard):
                self._recursiveDF(currBoard, nextBoard)  # go deep
            else:
                pass

        nextBoard = utils.placeNextBlack(currBoard, prvBoard, deepen=False)
        if not np.array_equal(nextBoard, prvBoard):
            self._recursiveDF(prvBoard, nextBoard)  # go horizontal
        else:
            pass

    def _astar(self):

        self._initialize()

        entryTime = time.process_time()
        self.iterations = 0

        self._recursiveAStar(self.board)

        exitTime = time.process_time()
        self.executionTime = exitTime - entryTime

    def _recursiveAStar(self, currBoard):

        if self.foundSolution:
            pass

        tempBoard = utils.placeNextBlack(currBoard, currBoard)
        nextBoard = []
        minHX = -np.inf

        while not np.array_equal(tempBoard, currBoard):
            self.iterations += 1
            hx = utils.heuristic(tempBoard)

            if (not utils.validate(tempBoard)) or hx > 0:
                tempBoard = utils.placeNextBlack(tempBoard, currBoard,
                                                 deepen=False)
                continue

            if hx == 0 and utils.isSolution(tempBoard):
                self.solvedBoard["board"] = tempBoard
                self.foundSolution = True
                break

            # all boards in list have the same heuristic (= best heuristic),
            # if better one is found -> new list
            elif hx == minHX and not utils.elemInList(tempBoard, nextBoard):
                nextBoard.append(tempBoard)

            # if better heuristic is found for a board -> create new list
            elif hx > minHX:
                nextBoard = [tempBoard]
                minHX = hx

            tempBoard = utils.placeNextBlack(tempBoard, currBoard,
                                             deepen=False)

        for i in range(len(nextBoard)):

            if minHX == 0:
                if utils.isSolution(nextBoard[i]):
                    self.solvedBoard["board"] = nextBoard[i]
                    break  # solution has been found so end loop and recursion
                else:
                    continue  # do not deepen, hx will not be closer to 0

            # continue search from next board onwards
            self._recursiveAStar(nextBoard[i])
