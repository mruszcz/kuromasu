# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:07:49 2019

@author: oem
"""


def white(x):
    if( x > 0 ):
        return 1
    else:
        return 0



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
    if( (board[row-1][col] == -1) or (board[row+1][col] == -1) or (board[row][col-1] == -1) or (board[row][col+1] == -1) ):
        return False
    else:
        return True
        
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
    return( cell[0] == 0 or cell[0] == noRow or cell[1] == 0 or cell[1] == noCol )