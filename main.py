from time import time

import numpy as np

import utils_kuro as utils


class Kuromasu:

    def __init__(self):
        self.board = np.array([[0, 0, 0, 0, 2],
                               [0, 0, 3, 0, 0]])
        
        #[[0, 0, 0, 0, 2],
        #                       [0, 0, 3, 0, 0]])
        #[[0, 0, 0, 0],
        # [3, 0, 2, 0],
        # [0, 3, 0, 4],
        # [0, 0, 0, 0]]
        self.solvedBoard = {"board": np.empty_like(self.board), "length": np.inf}  # shortest board

        self.executionTime = 0
        self.iterations = 0
        self.foundSolution = False

    def solve(self, mode):
        """Method for solvind the board
        Arguments: self, mode
        mode can be either A* or DF"""

        if mode is "Astar":
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
            if not np.array_equal(nextBoard, prvBoard):
                self._recursiveDF(currBoard, nextBoard)  # go deep
            else:
                pass

        nextBoard = self._placeNextBlack(currBoard, prvBoard, deepen=False)
        if not np.array_equal(nextBoard, prvBoard):
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


        while (board[y][x] != 1):  # find next viable position for black

            if x is (noCol - 1) and y is (noRow - 1):
                return prvBoard  # end of table, no viable positions

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

    ##############################################################

    def _astar(self):

        self.initialize()
        #self.solvedBoard["board"] = self.board

        entryTime = time()
        self.iterations = 0

        self._recursiveAStar(self.board)

        exitTime = time()

        self.executionTime = exitTime - entryTime

    def _recursiveAStar(self, currBoard):
        #gx = utils.length(self.solvedBoard["board"])
        #self.solvedBoard["length"] = gx

        if self.foundSolution:
            pass
        
        #### BETTER EMPTY LIST BECAUSE IF NOT POSSIBLE THAT NOT SOLVABLE BOARDS ARE IN LIST
        tempBoard = self._placeNextBlack(currBoard, currBoard)
        #nextBoard = [tempBoard]
        nextBoard = []
        minHX = -np.inf


        while (not np.array_equal(tempBoard, currBoard)):
            #### HX HAS TO BE FLOAT ### SOLVED
            hx = self._heuristic(tempBoard)
            
            if (not self._validate(tempBoard)) or hx > 0:
                tempBoard = self._placeNextBlack(
                    tempBoard, currBoard, deepen=False)
                continue
            
            ### exit while loop but no handling afterwards -> have to end program 
            if hx == 0 and utils.isSolution(tempBoard):
                self.solvedBoard["board"] = tempBoard
                self.foundSolution = True
                break
            
            ### all boards in list have the same heuristic (= best heuristic) if better one is found -> new list
            ### TEMP HAS TO BE COMPARED TO ALL. COULD BE SAME AS LATER ONE IN LIST
            ### COMPARE WITH MINHX INSTEAD OF [0] TO USE EMPTY LIST AT BEGINNING
            #elif hx == self._heuristic(nextBoard[0]) and not np.array_equal(tempBoard, nextBoard[0]):
            elif hx == minHX and not utils.elemInList(tempBoard, nextBoard):
                nextBoard.append(tempBoard)
            
            ### if better heuristic is found for a board -> create new list
            ### all elements will have same heuristic value (= minHX)
            elif hx > minHX:
                nextBoard = [tempBoard]
                minHX = hx

            tempBoard = self._placeNextBlack(
                tempBoard, currBoard, deepen=False)
            
        
        ### check all fields currently in list nextBoard
        for i in range(len(nextBoard)):
            ### continue to check other boards of list if hx = 0 but no solution
            #if minHX == 0 and not utils.isSolution(nextBoard[i]):
            #    continue
            
            ### solution was found so just pass?! 
            if minHX == 0:
                if utils.isSolution(nextBoard[i]):
                    self.solvedBoard["board"] = nextBoard[i]
                    break
                else:
                    continue
            
                        
            
            ### continue search from next board onwards
            #self.solvedBoard["board"] = nextBoard[i]
            ### if foundSolution = TRUE -> pass in recursiveAStar -> nextIteration of for loop?
            self._recursiveAStar(nextBoard[i])
        

    def _heuristic(self, board):
        reachable = 0
        goal = 0 

        for x in range(len(board)):
            row = board[x]
            for y in range(len(row)):
                # if field contains a number
                if row[y] > 1:
                    goal += row[y]
                    reachable += 1  # the field itself is counted
                    reachable += utils.countColumn(board, x, y)
                    reachable += utils.countRow(board, x, y)

        
        ratio = float(reachable)/float(goal)
        return (1-ratio)

                

game = Kuromasu()

game.solve("Astar")

print ("board :\n", game.board, "\n solved board: \n", game.solvedBoard["board"], "time: ",game.executionTime)
