import numpy as np
from time import time
import utils_kuro as utils

class Kuromasu:

    def __init__(self):
        self.board = np.array([[0, 0, 0, 0],
                      [2, 0, 2, 0],
                      [0, 3, 0, 4],
                      [0, 0, 0, 0]])
        self.solvedBoards = [] # list of solved boards

        self.executionTime = 0
        self.iterations = 0
        
    def solve(self, mode):
        """Method for solvind the board
        Arguments: self, mode
        mode can be either A* or DF"""


        if mode is "A*":
            # A* algortihm
            self.solvedBoard = self._astar()
        elif mode is "DF":
            # depth-first algorith
            self.solvedBoard = self._DF()
        else:
            Exception("Argument error! Wrong argument for solve method")

        return self.solvedBoard, self.exectutionTime, self.iterations

    def _validate(self):
        # checks board agianst rules of the game

        # returns boolean
        return True or False
    
    
    def _DF(self):
        """Implementation of depth-first algorithm"""
        self.initialize()  #whiten all

        entryTime = time()
        self.iterations = 0

        self._recursiveDF(self.board, self.board)

        exitTime = time()

        self.executionTime = exitTime - entryTime


    def _recursiveDF(self, prvBoard, currBoard):
        """Method finding all solutions to the puzzle, using recursive strategy"""
        self.iterations += 1

        if not utils.validate(currBoard):
            pass
        
        if utils.isSolution(currBoard): #found one solution
            self.solvedBoards.append(currBoard)


        nextBoard = utils.placeNextBlack(currBoard=currBoard, prvBoard=prvBoard)
        if nextBoard != currBoard:
            self._recursiveDF(currBoard, nextBoard)  #go deep
        else:
            pass
            
        nextBoard = utils.placeNextBlack(currBoard, prvBoard, deepen=False)
        if nextBoard != currBoard:
            self._recursiveDF(prvBoard, nextBoard)  #go horizontal
        else:
            pass
            


    def _placeNextBlack(currBoard, prvBoard, deepen=True):
        """Method for changing the game board by adding one black cell
        Returns currBoard if cannot place"""

        mask = currBoard - prvBoard
        board = currBoard

        noRow = len(board)
        noCol = len(board[0])

        x, y = utils.findPos(mask) #coords of last change

        if not deepen:
            board[x][y] = 1
            x += 1
            deepen = True

        while board[x][y] is not 1:  #find next viable position for black

            if x is (noCol - 1) and y is (noRow - 1):
                return currBoard  #end of table, no viable positions
                
            if not deepen:
                board[x][y] = 1
                deepen = True  #do only once at the beginning of loop only when broadening the tree

            if x is noCol - 1: #advance coords
                y += 1
                x = 0
            else:
                x += 0

        board[x][y] = -1
        
        return board