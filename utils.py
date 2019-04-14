import numpy as np


def isWhite(x):
    if x > 0:
        return True
    else:
        return False


def isBlack(x):
    if x == -1:
        return True
    else:
        return False


def countRow(board, row, col):
    cntWhite = 0

    # check all the fields left from the examined field
    y = col - 1
    while y >= 0:
        cell = board[row][y]
        if not isWhite(cell):
            break
        elif isWhite(cell):
            cntWhite += 1
        y -= 1

    # check all the fields right from the examined field
    y = col + 1
    while y < len(board[0]):
        cell = board[row][y]
        if not isWhite(cell):
            break
        elif isWhite(cell):
            cntWhite += 1
        y += 1

    return cntWhite


def countColumn(board, row, col):
    cntWhite = 0

    # check all the fields above the examined field
    x = row - 1
    while x >= 0:
        cell = board[x][col]
        if not isWhite(cell):
            break
        elif isWhite(cell):
            cntWhite += 1
        x -= 1

    # check all the fields below the examined field
    x = row + 1
    while x < len(board):
        cell = board[x][col]
        if not isWhite(cell):
            break
        elif isWhite(cell):
            cntWhite += 1
        x += 1
    return cntWhite


def checkAdjacentBlack(board, row, col):
    noRow = len(board) - 1
    noCol = len(board[0]) - 1

    if not row == 0:
        if isBlack(board[row - 1][col]):
            return True
    if not row == noRow:
        if isBlack(board[row + 1][col]):
            return True
    if not col == 0:
        if isBlack(board[row][col - 1]):
            return True
    if not col == noCol:
        if isBlack(board[row][col + 1]):
            return True

    return False


def searchBlackCircle(board, start, prev, cur, first):

    if (not first) and (start == cur):
        return True
    if not first and (separateBoard(board, start, cur)):
        return True
    first = False

    noRow = len(board) - 1
    noCol = len(board[0]) - 1

    if (not cur[0] == 0) and (not cur[1] == 0):
        x = cur[0] - 1
        y = cur[1] - 1
        # if no circle found
        if continueSearch(board, prev, x, y):
            if searchBlackCircle(board, start, cur, [x, y], first):
                return True
            else:
                return False

    if (not cur[1] == noCol) and (not cur[0] == 0):
        x = cur[0] - 1
        y = cur[1] + 1
        if continueSearch(board, prev, x, y):
            if searchBlackCircle(board, start, cur, [x, y], first):
                return True
            else:
                return False

    if (not cur[1] == 0) and (not cur[0] == noRow):
        x = cur[0] + 1
        y = cur[1] - 1
        # if no circle found
        if continueSearch(board, prev, x, y):
            if searchBlackCircle(board, start, cur, [x, y], first):
                return True
            else:
                return False

    if (not cur[1] == noCol) and (not cur[0] == noRow):
        x = cur[0] + 1
        y = cur[1] + 1
        if continueSearch(board, prev, x, y):
            if searchBlackCircle(board, start, cur, [x, y], first):
                return True
            else:
                return False


def continueSearch(board, prev, x, y):
    if (x >= 0 and x <= len(board) - 1 and
            y >= 0 and y <= len(board[0]) - 1):

        if board[x][y] == -1 and prev != [x, y]:
            return True
        else:
            return False
    else:
        return False


def separateBoard(board, start, cur):
    noRow = len(board) - 1
    noCol = len(board[0]) - 1

    return atEdge(start, noRow, noCol) and atEdge(cur, noRow, noCol)


def atEdge(cell, noRow, noCol):
    return cell[0] == 0 or cell[0] == noRow or cell[1] == 0 or cell[1] == noCol


def findPos(mask):
    noRow = len(mask)
    noCol = len(mask[0])
    for y in range(noRow):
        for x in range(noCol):
            if mask[y][x] != 0:
                return x, y


def length(board):
    print(board)
    len = 0
    with np.nditer(board) as iterator:
        for x in iterator:
            print(x)
            if x == (-1):
                len += 1

    return len


def isSolution(board):
    for x in range(len(board)):
        row = board[x]
        for y in range(len(row)):
            # if field contains a number
            if row[y] > 1:

                sumWhite = 1  # the field itself is counted
                sumWhite += countColumn(board, x, y)
                sumWhite += countRow(board, x, y)

                # if suurounding fields correspond
                if sumWhite != row[y]:
                    return False

    return True


def elemInList(tempBoard, boardList):
    for i in range(len(boardList)):
        if np.array_equal(tempBoard, boardList[i]):
            return True
        else:
            return False


def heuristic(self, board):
    reachable = 0
    goal = 0
    for x in range(len(board)):
        row = board[x]
        for y in range(len(row)):
            # if field contains a number
            if row[y] > 1:
                goal += row[y]
                reachable += 1  # the field itself is counted
                reachable += countColumn(board, x, y)
                reachable += countRow(board, x, y)
    ratio = float(reachable) / float(goal)
    return 1 - ratio


def _validate(self, board):
    """checks board agianst rules of the game.
    Returns True if board is coorect,
    False otherwise
    """
    for x in range(len(board)):
        row = board[x]
        for y in range(len(row)):
            if isBlack(row[y]):
                # check for black adjacent fields
                if checkAdjacentBlack(board, x, y):
                    return False
                # look for circles in the field
                if searchBlackCircle(board, [x, y], [x, y], [x, y],
                                     first=True):
                    return False
    return True


def _placeNextBlack(self, currBoard, prvBoard, deepen=True):
    """Function for changing the game board by adding one black cell
    on next viable position.
    Returns currBoard if cannot place"""

    mask = currBoard - prvBoard  # elementwise
    board = np.empty_like(currBoard)
    board = currBoard.copy()

    noRow = len(board)
    noCol = len(board[0])
    if not np.array_equal(currBoard, prvBoard):
        x, y = utils.findPos(mask)  # coords of last change
    else:  # entry case
        x = 0
        y = 0

    while board[y][x] != 1:  # find next viable position for black

        if x is (noCol - 1) and y is (noRow - 1):
            return prvBoard  # end of table, no viable positions

        if not deepen:
            board[y][x] = 1
            deepen = True  # do only once for broadening

        if x is noCol - 1:  # advance coords
            y += 1
            x = 0
        else:
            x += 1

    board[y][x] = -1

    return board
