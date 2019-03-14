# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 09:52:52 2019

@author: oem
"""

# implment depth first search algorithm to solve kuromasu

# Import required libraries.
import numpy as np
import scipy as sp

# black: -1
# grey: 0
# white: 1
# number: number

class Board:   
    def __init__(self):
        self.field = np.ndarray((4,4))
        self.field = [[-1, 0, 0, 0],
                      [2, -1, 2, 0],
                      [-1, 3, 0, 4],
                      [0, 0, 0, 0]]
    
    # fill all grey entries with white instead        
    def fill_white(self):
        for i in range(len(self.field)):
            row = self.field[i]
            for j in range(0, len(row)):
                if row[j] == 0:
                    self.field[i][j] = 1
                    
    def validate(self):
        for x in range(len(self.field)):
            row = self.field[x]
            for y in range(len(row)):
                # if field contains a number
                if (row[y] > 1):
                    sum_white = 1 # the field itself is counted
                    print "x:", x, "y:", y, "row:", row, "check:", row[y]
                    sum_white += count_column(self, x, y)
                    sum_white += count_row(self, x, y)
                    print sum_white


def count_row(self, row, col):
    ws = 0
    
    # check all the fields above the examined field 
    y = col-1
    while(y >= 0):
        if(self.field[row][y] < 0):
            break
        elif(self.field[row][y] >= 1):
            ws += 1
        y -= 1
    
    y = col +1    
    # check all the fields below the examined field
    while(y < len(self.field[0])):
        if(self.field[row][y] < 0):
            break
        elif(self.field[row][y] >= 1):
            ws += 1
        y += 1
    return ws
                
def count_column(self, row, col):
    ws = 0
    # check all the fields above the examined field 
    x = row -1
    while( x >= 0):
        if(self.field[x][col] < 0):
            break
        elif(self.field[x][col] >= 1):
            ws += 1
        x -= 1
    # check all the fields below the examined field
    x = row +1
    while(x < len(self.field)):
        if(self.field[x][col] < 0):
            break
        elif(self.field[x][col] >= 1):
            ws += 1
        x += 1
    return ws
 
     
               

def main():
    my_board = Board()
    my_board.fill_white()
    my_board.validate()

if __name__ == "__main__":
    main()