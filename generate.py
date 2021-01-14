from random import shuffle

N=9
#board = [[0, 8, 4, 1, 0, 0, 0, 0, 0], 
#            [3, 0, 0, 0, 0, 0, 0, 2, 0], 
#            [7, 0, 0, 9, 0, 0, 0, 0, 0], 
#            [0, 2, 0, 8, 0, 3, 0, 1, 6], 
#            [0, 0, 0, 0, 0, 7, 9, 0, 3], 
#            [6, 0, 0, 0, 0, 9, 5, 0, 0], 
#            [0, 1, 0, 0, 6, 0, 0, 0, 5], 
#            [2, 0, 0, 0, 0, 0, 0, 6, 1],
#            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

board = [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        
finalBoard = []

def setFinalBoard():
    for row in board:
        finalBoard.append(row.copy())

def updateBoard():
    board.clear()
    #print(board)
    for row in finalBoard:
        board.append(row.copy())
        #print(board)
    #print("UPDATING BOARD: ")
    #printBoard()

def printBoard():
    print('\n'.join([''.join(['{:4}'.format(col) for col in row]) 
            for row in board]))

def printFinalBoard():
    print('\n'.join([''.join(['{:4}'.format(col) for col in row]) 
            for row in finalBoard]))

def isSafe(row,col,num):
    for i in range(0,N):
        if i!=row and board[i][col]==num:
            return False
    for j in range(0,N):
        if j!=col and board[row][j]==num:
            return False
    startingRow = (N//3)*(row//(N//3))
    startingCol = (N//3)*(col//(N//3))
    for a in range(startingRow,startingRow+3):
        for b in range(startingCol,startingCol+3):
            if (a!=row or b!=col) and board[a][b]==num:
                return False
    return True
        
def getUnassigned(row,col):
    for a in range(row,N):
        for b in range(0,N):
            if board[a][b]==0:
                return (a,b)
    return (-1,-1)

def solve():
    #printBoard()
    global valid
    for i in range(0,81):
        row=i//9
        col=i%9
        if board[row][col]==0:
            for val in range(1,10):
                if isSafe(row,col,val):
                    board[row][col] = val
                    if isFilled():
                        valid+=1
                        if valid>1:
                            return False
                        break
                    elif not(solve()):
                        #print("TRUE")
                        return False
            break
    board[row][col] = 0





  #  unassigned = getUnassigned(row,col)
  #  if unassigned[0]==-1:
  #      return True
  #  for i in range(1,N+1):
  #      if isSafe(unassigned[0],unassigned[1],i):
  #          #print(i)
  #          board[unassigned[0]][unassigned[1]] = i
  #          if unassigned[0]==N-1 and unassigned[1]==N-1:
  #              global valid
  #              valid += 1
  #              if valid > 1:
  #                  return False
  #          elif unassigned[1]==N-1:
  #              if solve(unassigned[0]+1,0):
  #                  return True
  #          else:
  #              if solve(unassigned[0],unassigned[1]+1):
  #                  return True
  #  board[unassigned[0]][unassigned[1]] = 0
  #  return False

numbers = [1,2,3,4,5,6,7,8,9]
shuffle(numbers)
print(numbers)

def isFilled():
    for a in range(0,N):
        for b in range(0,N):
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

def shufflePositions():
    positions = []
    for i in range(0,81):
        row = i//9
        col=i%9
        positions.append((row,col,board[row][col]))
    shuffle(positions)
    return positions

def removeEntries(positions):
    global valid
    for curr in positions:
        updateBoard()
        print(curr)
        board[curr[0]][curr[1]] = 0
        #printBoard()
        #print()
        #printFinalBoard()
        valid=0
        solve()
        print(valid)
        if valid==1:
            print("VALID")
            finalBoard[curr[0]][curr[1]] = 0

def generateBoard():
    fillBoard()
    setFinalBoard()
    removeEntries(shufflePositions())
    return finalBoard
               
#
#printBoard()
#print()
#fillBoard()
#valid = 0
#printBoard()
##solve()
##print(valid)
#print()
#setFinalBoard()
#printFinalBoard()
#removeEntries(shufflePositions())
##printBoard()
#
#print()
#printFinalBoard()
