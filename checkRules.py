# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 09:52:52 2019

@author: oem
"""

# implment depth first search algorithm to solve kuromasu

# Import required libraries.
import numpy as np
import scipy as sp
import utils_kuro as uk

# black: -1
# grey: 0
# white: 1
# number: number

class Board:   
    def __init__(self):
        self.board = np.array([[0, 2, 0, 0, -1, 0, 0], 
                               [0, 0, 0, -1, 0, -1, 0],
                               [0, 0, -1, 0, 0, 0, -1],
                               [0, -1, 0, 0, 0, -1, 0],
                               [-1, 0, 0, 0, -1, 0, 0],
                               [0, -1, 0 -1, 0, 0, 0], 
                               [0, 0, -1, 0, 0, 0, 0]])
        self.solvedBoard = np.ndarray((4,4))
        self.valid = True
        
    # substitute all grey entries with white instead        
    def fill_white(self):
        for i in range(len(self.board)):
            row = self.board[i]
            for j in range(0, len(row)):
                if row[j] == 0:
                    self.board[i][j] = 1
                    
    def validate(self):

        # check number of white surrounding fields
        # return FALSE if not all the white fields have the neccessary number of surrounding white fields
        # return TRUE if all number fields have corresponding number of white surrounders
        # then set solvedBoard to currentBoard
        self.solvedBoard = np.zeros((4,4))
        solvedWhite = self.checkSurround()
        print "solvedWhite", solvedWhite, "valid", self.valid
        if( solvedWhite and self.valid ):
            self.solvedBoard = self.board
               
    
    def checkSurround(self):
        solvedWhite = True
        for x in range(len(self.board)):
            row = self.board[x]
            for y in range(len(row)):
                # if field contains a number
                if (row[y] > 1):
                    sumWhite = 1 # the field itself is counted
                    print "x:", x, "y:", y, "row:", row, "check:", row[y]
                    sumWhite += uk.count_column(self.board, x, y)
                    sumWhite += uk.count_row(self.board, x, y)
                    print sumWhite
                    # if suurounding fields correspond 
                    if(sumWhite != row[y] ):
                        solvedWhite = False
                    if( sumWhite is 1 ):
                        self.valid = False
                
                if ( row[y] == -1 and self.valid):
                    # check for black adjacent fields
                    self.valid = uk.checkAdjacenBlack(self.board, x, y)
                    
                    # look for circles in the field
                    if(self.valid):
                        if( self.searchBlackCircle([x,y], [x,y], [x,y], first = True) ):
                            self.valid = False
                            print "i found a circle"
                            return solvedWhite
                    else:
                        return solvedWhite
        return solvedWhite
    
    def searchBlackCircle(self, start, prev, cur, first):
        print "looking for circles now"
        if( (not first) and (start == cur) ):
            return True
        if( uk.separateBoard(self.board, start, cur) ):
            return True
        first = False
        x = cur[0] - 1
        y = cur[1] - 1
        # if no circle found
        print "x", x, "y", y, "cur", cur, "prev", prev, "start", start, self.board[x][y]
        if( uk.continueSearch(self.board, prev, x, y) ):
            if( self.searchBlackCircle(start, cur, [x, y], first) ): return True
        
        y = cur[1] + 1
        print "x", x, "y", y, "cur", cur, "prev", prev, "start", start, self.board[x][y]
        if( uk.continueSearch(self.board, prev, x, y) ):
            if( self.searchBlackCircle(start, cur, [x, y], first) ): return True
        
        x = cur[0] + 1
        y = cur[1] - 1
        print "x", x, "y", y, "cur", cur, "prev", prev, "start", start, self.board[x][y]
        # if no circle found
        if( uk.continueSearch(self.board, prev, x, y) ):
            if( self.searchBlackCircle(start, cur, [x, y], first) ): return True
        
        y = cur[1] + 1
        print "x", x, "y", y, "cur", cur, "prev", prev, "start", start, self.board[x][y]
        if( uk.continueSearch(self.board, prev, x, y) ):
            if( self.searchBlackCircle(start, cur, [x, y], first) ): return True
               

def main():
    my_board = Board()
    my_board.fill_white()
    my_board.validate()

if __name__ == "__main__":
    main()