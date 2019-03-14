import numpy as np

class Board:

    def __init__(self):
        self.board = np.array()
        self.solvedBoard = np.array()

        self.exectutionTime = 0
        
    def solve(self, mode):
        if mode is "A*":
            # A* algortihm
            self.solvedBoard = self._astar()
        elif mode is "DF":
            # depth-first algorith
            self.solvedBoard = self._DF()
        else:
            Exception("Argiment error! Wrong argument for solve method")

        return self.solvedBoard, self.exectutionTime

    def _checkRules(self):
        # checks board agianst rules of the game

        # returns boolean
        return True or False
    
    def _DF(self):
        # initilize board

        # pick black cell coordinates

        # check against rules

        # deepen
        # RECURSIVE?


    
