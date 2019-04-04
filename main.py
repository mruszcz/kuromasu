import numpy as np
from time import time
from math import inf
import utils_kuro as utils


class Kuromasu:

    def __init__(self):
        self.board = np.array([[0, 0, 0, 0, 2],
                               [0, 0, 3, 0, 0]])
        self.solvedBoard = {"board": np.empty_like(
            self.board), "length": inf}  # shortest board

        self.executionTime = 0
        self.iterations = 0

    def solve(self, mode):
        """Method for solvind the board
        Arguments: self, mode
        mode can be either A* or DF"""

        if mode is "A*":
            # A* algortihm
            self._astar()

        elif mode is "DF":
            # depth-first algorithm
            self._DF()

        else:
            Exception("Argument error! Wrong argument for solve method")

    def isShorter(self, board):

        return (utils.length(board) < self.solvedBoard["length"])

    def initialize(self):
        for i in range(len(self.board)):
            row = self.board[i]
            for j in range(0, len(row)):
                if row[j] == 0:
                    self.board[i][j] = 1

    def _validate(self, board):

        # checks board agianst rules of the game
        for x in range(len(board)):
            row = board[x]
            for y in range(len(row)):
                if utils.isBlack(row[y]):
                    # check for black adjacent fields
                    if utils.checkAdjacentBlack(board, x, y):
                        return False

                    # look for circles in the field
                    if utils.searchBlackCircle(board, [x, y], [x, y], [x, y], first=True):
                        return False
        # returns boolean
        return True

    def _DF(self):
        """Implementation of depth-first algorithm"""
        self.initialize()  # whiten all

        entryTime = time()
        self.iterations = 0

        self._recursiveDF(self.board, self.board)

        exitTime = time()

        self.executionTime = exitTime - entryTime

    def _recursiveDF(self, prvBoard, currBoard):
        """Method finding shortest solution to the puzzle, using recursive strategy"""
        self.iterations += 1
        print('iterations: {}'.format(self.iterations))

        if self._validate(currBoard):

            # found shorter solution
            if utils.isSolution(currBoard) and self.isShorter(currBoard):
                self.solvedBoard["board"] = currBoard
                self.solvedBoard["length"] = utils.length(currBoard)

            nextBoard = self._placeNextBlack(
                currBoard=currBoard, prvBoard=prvBoard)
            if not np.array_equal(nextBoard, currBoard):
                self._recursiveDF(currBoard, nextBoard)  # go deep
            else:
                pass

        nextBoard = self._placeNextBlack(currBoard, prvBoard, deepen=False)
        if not np.array_equal(nextBoard, currBoard):
            self._recursiveDF(prvBoard, nextBoard)  # go horizontal
        else:
            pass

    def _placeNextBlack(self, currBoard, prvBoard, deepen=True):
        """Method for changing the game board by adding one black cell
        Returns currBoard if cannot place"""

        mask = currBoard - prvBoard
        board = np.empty_like(currBoard)
        board = currBoard.copy()

        noRow = len(board)
        noCol = len(board[0])
        if not np.array_equal(currBoard, prvBoard):
            x,y = utils.findPos(mask)  # coords of last change
        else:  # entry case
            x = 0
            y = 0

        # if not deepen:
        #     board[y][x] = 1
        #     y += 1
        #     deepen = True

        while (board[y][x] != 1):  # find next viable position for black

            if x is (noCol - 1) and y is (noRow - 1):
                return currBoard  # end of table, no viable positions

            if not deepen:
                board[y][x] = 1
                deepen = True  # do only once at the beginning of loop only when broadening the tree

            if x is noCol - 1:  # advance coords
                y += 1
                x = 0
            else:
                x += 1

        board[y][x] = -1

        return board


game = Kuromasu()

game.solve("DF")

print("board :", game.board, "\n", "solved board: ", game.solvedBoard, "time: ",game.executionTime)
