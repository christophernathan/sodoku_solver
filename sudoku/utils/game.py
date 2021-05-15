import pygame
import sys
from time import sleep
from sudoku.utils import generate, draw

WIDTH=600
HEIGHT=800
white = (255,255,255)
black = (0,0,0)

board = [[0, 8, 4, 1, 0, 0, 0, 0, 0], 
            [3, 0, 0, 0, 0, 0, 0, 2, 0], 
            [7, 0, 0, 9, 0, 0, 0, 0, 0], 
            [0, 2, 0, 8, 0, 3, 0, 1, 6], 
            [0, 0, 0, 0, 0, 7, 9, 0, 3], 
            [6, 0, 0, 0, 0, 9, 5, 0, 0], 
            [0, 1, 0, 0, 6, 0, 0, 0, 5], 
            [2, 0, 0, 0, 0, 0, 0, 6, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 7]]
originalBoard = []
interactiveBoard = []
for row in board:
    originalBoard.append(row.copy())
    interactiveBoard.append(row.copy())

def loadNewBoard(newBoard): # load newly-generated board
    board.clear()
    originalBoard.clear()
    interactiveBoard.clear()
    for row in newBoard:
        board.append(row.copy())
        originalBoard.append(row.copy())
        interactiveBoard.append(row.copy())

def calcBox(): # calculate which board cell is clicked
    mouse = pygame.mouse.get_pos()
    return ((mouse[1]-3)//((WIDTH-6)/9),(mouse[0]-3)//((WIDTH-6)/9))

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
        
def getUnassigned(row,col): # retrieves an unassigned cell
    for a in range(row,9):
        for b in range(0,9):
            if board[a][b]==0:
                return (a,b)
    return (-1,-1)

def solve(gameDisplay,row,col,startTime,checkWork): # recursive solve function
    if not checkWork: # monitor for quit signal
        draw.drawTimer(gameDisplay,startTime)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
    unassigned = getUnassigned(row,col)
    if unassigned[0]==-1:
        return True
    for i in range(1,10): # loops through digits to see which are valid
        if isSafe(unassigned[0],unassigned[1],i):
            if not checkWork: # draw new valid number in cell
                draw.removeInvalid(gameDisplay,unassigned[0],unassigned[1])
                draw.addValid(gameDisplay,unassigned[0],unassigned[1],i)
            board[unassigned[0]][unassigned[1]] = i
            if unassigned[0]==8 and unassigned[1]==8: # board is valid and complete
                return True
            elif unassigned[1]==8: # solve starting on next row
                if solve(gameDisplay, unassigned[0]+1,0, startTime, checkWork):
                    return True
            else: # solve starting on next col
                if solve(gameDisplay, unassigned[0],unassigned[1]+1, startTime, checkWork):
                    return True
    board[unassigned[0]][unassigned[1]] = 0
    if not checkWork: # if no digit is valid in consideration of other cells
        draw.removeInvalid(gameDisplay,unassigned[0],unassigned[1])
    return False

def executeSolve(gameDisplay, startTime, checkWork):
    solve(gameDisplay,0,0,startTime,checkWork)

def resetBoard(gameDisplay):
    gameDisplay.fill(white)
    draw.drawBoard(gameDisplay)
    for a in range(9):
        for b in range(9):
            board[a][b] = originalBoard[a][b]
            interactiveBoard[a][b] = originalBoard[a][b]
            if originalBoard[a][b]!=0:
                draw.addValid(gameDisplay,a,b,originalBoard[a][b])
    pygame.display.update()

def handleUserInput(gameDisplay, row,col):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9:
                    interactiveBoard[int(row)][int(col)] = event.key-48
                    draw.removeInvalid(gameDisplay,row,col)
                    draw.addValid(gameDisplay,row,col,event.key-48)
                elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                    interactiveBoard[int(row)][int(col)] = 0
                    draw.removeInvalid(gameDisplay,row,col)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                draw.drawInnerBox(gameDisplay,white,row,col,2)
                pygame.display.update()
                handleClick(gameDisplay)
                return
        draw.drawInnerBox(gameDisplay,black,row,col,2)
        pygame.display.update()
        
def checkWork(gameDisplay): # check which user-entered numbers are correct and incorrect in comparison with the valid solution
    executeSolve(gameDisplay, 0, True)
    complete = True
    for a in range(9):
        for b in range(9):
            if originalBoard[a][b]==0 and interactiveBoard[a][b]!=0:
                if interactiveBoard[a][b] == board[a][b]:
                    draw.drawInnerBox(gameDisplay,draw.green,a,b,2)
                else:
                    complete = False
                    draw.drawInnerBox(gameDisplay,draw.dark_red,a,b,2)
            elif interactiveBoard[a][b]==0:
                complete = False
    if complete:
        draw.drawComplete(gameDisplay)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for a in range(9):
                    for b in range(9):
                        draw.drawInnerBox(gameDisplay,white,a,b,2)
                draw.removeComplete(gameDisplay)
                handleClick(gameDisplay)
                return

def handleClick(gameDisplay): # triggered if user clicks
    mouse = pygame.mouse.get_pos()
    if WIDTH/10 <= mouse[0] <= 3*WIDTH/10 and WIDTH+(HEIGHT-WIDTH)/6 <= mouse[1] <= WIDTH+(HEIGHT-WIDTH)/2: # solve
        resetBoard(gameDisplay)
        startTime = pygame.time.get_ticks()
        draw.drawButtons(gameDisplay)
        draw.drawTimer(gameDisplay,startTime)
        executeSolve(gameDisplay, startTime, False)
        draw.drawTimer(gameDisplay,startTime)
    elif 4*WIDTH/10 <= mouse[0] <= 6*WIDTH/10 and WIDTH+(HEIGHT-WIDTH)/6 <= mouse[1] <= WIDTH+(HEIGHT-WIDTH)/2: # check
        checkWork(gameDisplay)
    elif 7*WIDTH/10 <= mouse[0] <= 9*WIDTH/10 and WIDTH+(HEIGHT-WIDTH)/6 <= mouse[1] <= WIDTH+(HEIGHT-WIDTH)/2: # new board
        newBoard = generate.generateBoard()
        loadNewBoard(newBoard)
        resetBoard(gameDisplay)
    elif 7*WIDTH/10 <= mouse[0] <= 9*WIDTH/10 and WIDTH+4*(HEIGHT-WIDTH)/6 <= mouse[1] <= WIDTH+5*(HEIGHT-WIDTH)/6: # reset
        resetBoard(gameDisplay)
    elif 3 <= mouse[0] <= WIDTH-3 and 3 <= mouse[1] <= WIDTH-3:
        box = calcBox()
        if originalBoard[int(box[0])][int(box[1])]==0:
            handleUserInput(gameDisplay,box[0],box[1])
