# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:07:49 2019

@author: oem
"""
import numpy as np

def white(x):
    if( x > 0 ):
        return 1
    else:
        return 0
        
def black(x):
    if(x == -1):
        return 1
    else:
        return 0

def isSolution(board):
    solvedWhite = True
    for x in range(len(board)):
        row = board[x] 
        for y in range(len(row)):
            # if field contains a number
            if (row[y] > 1):
                sumWhite = 1 # the field itself is counted
                sumWhite += count_column(board, x, y)
                sumWhite += count_row(board, x, y)
                # if suurounding fields correspond 
                if(sumWhite != row[y] ):
                    solvedWhite = False
#                if( sumWhite is 1 ):
#                    self.valid = False
    return solvedWhite

def count_row(board, row, col):
    cntWhite = 0
    
    # check all the fields left from the examined field 
    y = col-1
    while(y >= 0):
        cell = board[row][y]
        if( not white(cell) ):
            break
        elif( white(cell) ):
            cntWhite += 1    
        y -= 1
   
    # check all the fields right from the examined field
    y = col +1    
    while(y < len(board[0])):
        cell = board[row][y]
        if( not white(cell) ):
            break
        elif( white(cell) ):
            cntWhite += 1
        y += 1
        
    return cntWhite
                
def count_column(board, row, col):
    cntWhite = 0
    
    # check all the fields above the examined field 
    x = row -1
    while( x >= 0):
        cell = board[x][col]
        if( not white(cell) ):
            break
        elif( white(cell) ):
            cntWhite += 1
        x -= 1
        
    # check all the fields below the examined field
    x = row +1
    while(x < len(board)):
        cell = board[x][col]
        if( not white(cell) ):
            break
        elif( white(cell) ):
            cntWhite += 1
        x += 1
    return cntWhite
    
def checkAdjacenBlack(board, row, col):
    noRow = len(board) - 1
    noCol = len(board[0]) -1
    if(not row == 0):
        if( black(board[row-1][col]) ): return False
    if( not row == noRow):
        if( black(board[row+1][col]) ): return False
    if( not col == 0 ):
        if( black(board[row][col-1]) ): return False
    if( not col == noCol ):
        if( black(board[row][col+1]) ): return False
    else:
        return True

def searchBlackCircle(board, start, prev, cur, first):

    if( (not first) and (start == cur) ):
        print "i am back at the beinning and found circle from: ", start, "prev", prev, "end", cur
        return True
    if( (not first) and (uk.separateBoard(self.board, start, cur)) ):
        return True
    first = False
    
    x = cur[0] - 1
    y = cur[1] - 1
    # if no circle found
    print "x", x, "y", y, "cur", cur, "prev", prev, "start", start, self.board[x][y]
    if( continueSearch(board, prev, x, y) ):
        if( searchBlackCircle(start, cur, [x, y], first) ): return True
        else: return False
    
    y = cur[1] + 1
    print "x", x, "y", y, "cur", cur, "prev", prev, "start", start, self.board[x][y]
    if( continueSearch( board, prev, x, y) ):
        if( searchBlackCircle(start, cur, [x, y], first) ): return True
        else: return False
    
    x = cur[0] + 1
    y = cur[1] - 1
    print "x", x, "y", y, "cur", cur, "prev", prev, "start", start, self.board[x][y]
    # if no circle found
    if( continueSearch( board, prev, x, y) ):
        if( searchBlackCircle(start, cur, [x, y], first) ): return True
        else: return False
    
    y = cur[1] + 1
    print "x", x, "y", y, "cur", cur, "prev", prev, "start", start, self.board[x][y]
    if( continueSearch( board, prev, x, y) ):
        if( searchBlackCircle(start, cur, [x, y], first) ): return True
        else: return False

        
def continueSearch( board, prev, x, y ):
    if( (x >= 0 and x <= len(board)-1) and (y >= 0 and y <= len(board[0])-1 )):
        if( (board[x][y] == -1) and (prev != [x, y]) ):
            return True
        else:
            return False
    else: return False

def separateBoard(board, start, cur):
    noRow = len(board) -1
    noCol = len(board[0]) -1        
    return( uk.atEdge(start, noRow, noCol) and uk.atEdge(cur, noRow, noCol))
        
        
def atEdge(cell, noRow, noCol):
    return (cell[0] == 0 or cell[0] == noRow or cell[1] == 0 or cell[1] == noCol)

def findPos(mask):
    noRow = len(mask)
    noCol = len(mask[0])

    for y in range(noRow):
        for x in range(noCol):
            if mask[y][x] is 1:
                return x, y
                
def length(board):
    len = 0
    with np.nditer(board) as iterator:
        for x in iterator:
            if x is - 1:
                len += 1
    
    return len