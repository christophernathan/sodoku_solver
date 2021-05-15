board = [[0, 8, 4, 1, 0, 0, 0, 0, 0], 
            [3, 0, 0, 0, 0, 0, 0, 2, 0], 
            [7, 0, 0, 9, 0, 0, 0, 0, 0], 
            [0, 2, 0, 8, 0, 3, 0, 1, 6], 
            [0, 0, 0, 0, 0, 7, 9, 0, 3], 
            [6, 0, 0, 0, 0, 9, 5, 0, 0], 
            [0, 1, 0, 0, 6, 0, 0, 0, 5], 
            [2, 0, 0, 0, 0, 0, 0, 6, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 7]]

def printBoard(board):
    for r in board:
        print(r)

def isSafe(row,col,num): # determines if the given number is valid in the given cell
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

def cellPossibleValues(board, row=0, col=0):
    nums=[]
    if board[row][col]!=0:
        nums.append(board[row][col])
        return nums
    printBoard(board)
    nums = [1,2,3,4,5,6,7,8,9]
    for i in range(0,9):
        if i!=row and board[i][col] in nums:
            nums.remove(board[i][col])
    for j in range(0,9):
        if j!=col and board[row][j] in nums:
            nums.remove(board[row][j])
    startingRow = 3*(row//3)
    startingCol = 3*(col//3)
    for a in range(startingRow,startingRow+3):
        for b in range(startingCol,startingCol+3):
            if (a!=row or b!=col) and board[a][b] in nums:
                nums.remove(board[a][b])
    print(nums)
    return nums


def getPossibleValues(board):
    possibleValues = []
    for a in range(0,9):
        row = []
        for b in range(0,9):
            row.append(cellPossibleValues(board,a,b))
        possibleValues.append(row)
    for r in possibleValues:
        print(r)

getPossibleValues(board)