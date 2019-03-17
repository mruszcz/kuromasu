# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:07:49 2019

@author: oem
"""
import numpy as np
from main import Board

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
    if( (board[x][y] == -1) and (prev != [x, y]) ):
        return True
    else:
        return False

def separateBoard(board, start, cur):
    noRow = len(board)
    noCol = len(board[0])
    if( (start[0] == 0 and cur[0] == 0) or (start[0] == 0 and cur[0]== noRow-1) or 
    (start[0] == noRow-1 and cur[0]==0) or (start[0] == noRow-1 and cur[0]== noRow-1) or 
    (start[1] == 0 and cur[1] == 0) or (start[1] == 0 and cur[1]== noCol-1) or 
    (start[1] == noCol-1 and cur[1]==0) or (start[1] == noCol-1 and cur[1]== noCol-1) ):
        return True
    else:
        return False


def findPos(mask):
    noRow = len(mask)
    noCol = len(mask[0])

    for y in range(noRow):
        for x in range(noCol):
            if mask[y][x] is 1:
                return x,y