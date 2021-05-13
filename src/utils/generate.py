from random import shuffle

board = []
finalBoard = []
        
numbers = [1,2,3,4,5,6,7,8,9]

def resetBoard():
    board.clear()
    for i in range(0,9):
        board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

def setFinalBoard():
    finalBoard.clear()
    for row in board:
        finalBoard.append(row.copy())

def updateBoard():
    board.clear()
    for row in finalBoard:
        board.append(row.copy())

def isSafe(row,col,num): # determines if a given number is valid in the given position
    for i in range(0,9):
        if i!=row and board[i][col]==num:
            return False
    for j in range(0,9):
        if j!=col and board[row][j]==num:
            return False
    startingRow = 3*(row//3)
    startingCol = 3*(col//3)
    for a in range(startingRow,startingRow+3):
        for b in range(startingCol,startingCol+3):
            if (a!=row or b!=col) and board[a][b]==num:
                return False
    return True

def solve():
    global valid
    for i in range(0,81):
        row=i//9
        col=i%9
        if board[row][col]==0:
            for val in range(1,10):
                if isSafe(row,col,val):
                    board[row][col] = val
                    if isFilled():
                        valid+=1 # valid board solution found
                        if valid>1: # exit recursive solve loop if there is not 1 unique board solution
                            return False
                        break
                    elif not(solve()): # exits loop immediately when a second board solution is found
                        return False
            break
    board[row][col] = 0
    return True # Want to backtrack to check for uniqueness instead of exiting loop immediately

def isFilled():
    for a in range(0,9):
        for b in range(0,9):
            if board[a][b]==0:
                return False
    return True

def fillBoard():
    for i in range(0,81):
        row=i//9
        col=i%9
        if board[row][col]==0:
            shuffle(numbers)
            for n in numbers:
                if isSafe(row,col,n):
                    board[row][col] = n
                    if isFilled():
                        return True
                    elif fillBoard():
                        return True
            break
    board[row][col] = 0

def shufflePositions(): # randomizes elimination of numbers from a full board
    positions = []
    for i in range(0,81):
        row = i//9
        col=i%9
        positions.append((row,col,board[row][col]))
    shuffle(positions)
    return positions

def removeEntries(positions): # removes numbers from board one by one in random order, leaving a final board with minimum numbers remaining to preserve uniqueness
    global valid
    for curr in positions:
        updateBoard()
        board[curr[0]][curr[1]] = 0
        valid=0
        solve()
        if valid==1: # if there is 1 unique solution to the current board
            finalBoard[curr[0]][curr[1]] = 0

def generateBoard():
    resetBoard()
    fillBoard()
    setFinalBoard()
    removeEntries(shufflePositions())
    return finalBoard