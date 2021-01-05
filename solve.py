import pygame
import pygame.freetype
import sys
from time import sleep
N=9
WIDTH=600
HEIGHT=800
white = (255,255,255)
black = (0,0,0)
light_grey = (200,200,200)
dark_grey = (100,100,100)
blue = (0,0,255)
red = (255,0,0)
board = [[0, 8, 4, 1, 0, 0, 0, 0, 0], 
            [3, 0, 0, 0, 0, 0, 0, 2, 0], 
            [7, 0, 0, 9, 0, 0, 0, 0, 0], 
            [0, 2, 0, 8, 0, 3, 0, 1, 6], 
            [0, 0, 0, 0, 0, 7, 9, 0, 3], 
            [6, 0, 0, 0, 0, 9, 5, 0, 0], 
            [0, 1, 0, 0, 6, 0, 0, 0, 5], 
            [2, 0, 0, 0, 0, 0, 0, 6, 1], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]
originalBoard = []
for row in board:
    originalBoard.append(row.copy())

pygame.init()
BOARD_FONT = pygame.font.SysFont("newyork", 50)
BUTTON_FONT = pygame.font.SysFont("newyork", 20)

def drawRectangle(gameDisplay,color,left,top,width,height,thickness):
    pygame.draw.rect(gameDisplay,color,(left,top,width,height),thickness)

def addValid(gameDisplay,row,col,num):
    box_width = (WIDTH-6)/9
    text = BOARD_FONT.render(str(num), True, black)
    text_width = text.get_rect().width
    text_height = text.get_rect().height
    gameDisplay.blit(text,(3+col*box_width+((box_width-text_width)/2),3+row*box_width+((box_width-text_height)/2)))
    pygame.display.update()
    #sleep(.01)

def removeInvalid(gameDisplay,row,col):
    box_width = (WIDTH-6)/9
    drawRectangle(gameDisplay,white,6+col*box_width,6+row*box_width,box_width-6,box_width-6,0)
    pygame.display.update()
    #sleep(.01)

def drawBoard(gameDisplay):
    lineThickness = 1
    drawRectangle(gameDisplay,black,3,3,WIDTH-6,WIDTH-6,3)
    for a in range(3):
        for b in range(3):
            drawRectangle(gameDisplay,black,3+b*(WIDTH-6)/3,3+a*(WIDTH-6)/3,(WIDTH-6)/3,(WIDTH-6)/3,2)
    for a in range(9):
        for b in range(9):
            drawRectangle(gameDisplay,black,3+b*(WIDTH-6)/9,3+a*(WIDTH-6)/9,(WIDTH-6)/9,(WIDTH-6)/9,1)

def printBoard():
    print('\n'.join([''.join(['{:4}'.format(col) for col in row]) 
            for row in board]))

def printOriginal():
    print('\n'.join([''.join(['{:4}'.format(col) for col in row]) 
            for row in originalBoard]))

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

def solve(gameDisplay,row,col):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
    unassigned = getUnassigned(row,col)
    if unassigned[0]==-1:
        return True
    for i in range(1,N+1):
        if isSafe(unassigned[0],unassigned[1],i):
            #print(i)
            removeInvalid(gameDisplay,unassigned[0],unassigned[1])
            addValid(gameDisplay,unassigned[0],unassigned[1],i)
            board[unassigned[0]][unassigned[1]] = i
            if unassigned[0]==N-1 and unassigned[1]==N-1:
                return True
            elif unassigned[1]==N-1:
                if solve(gameDisplay, unassigned[0]+1,0):
                    return True
            else:
                if solve(gameDisplay, unassigned[0],unassigned[1]+1):
                    return True
    board[unassigned[0]][unassigned[1]] = 0
    removeInvalid(gameDisplay,unassigned[0],unassigned[1])
    return False

def executeSolve(gameDisplay):
    solve(gameDisplay,0,0)

def handleButtons(gameDisplay):
    mouse = pygame.mouse.get_pos()
    BUTTON_WIDTH = WIDTH/5
    BUTTON_HEIGHT = (HEIGHT-WIDTH)/3
    if WIDTH/10 <= mouse[0] <= 3*WIDTH/10 and WIDTH+(HEIGHT-WIDTH)/6 <= mouse[1] <= WIDTH+(HEIGHT-WIDTH)/2: 
        pygame.draw.rect(gameDisplay,light_grey,[WIDTH/10,WIDTH+(HEIGHT-WIDTH)/6,BUTTON_WIDTH,BUTTON_HEIGHT])
    else:
        pygame.draw.rect(gameDisplay,dark_grey,[WIDTH/10,WIDTH+(HEIGHT-WIDTH)/6,BUTTON_WIDTH,BUTTON_HEIGHT])
    if 4*WIDTH/10 <= mouse[0] <= 6*WIDTH/10 and WIDTH+(HEIGHT-WIDTH)/6 <= mouse[1] <= WIDTH+(HEIGHT-WIDTH)/2: 
        pygame.draw.rect(gameDisplay,light_grey,[4*WIDTH/10,WIDTH+(HEIGHT-WIDTH)/6,BUTTON_WIDTH,BUTTON_HEIGHT])
    else:
        pygame.draw.rect(gameDisplay,dark_grey,[4*WIDTH/10,WIDTH+(HEIGHT-WIDTH)/6,BUTTON_WIDTH,BUTTON_HEIGHT])
    if 7*WIDTH/10 <= mouse[0] <= 9*WIDTH/10 and WIDTH+(HEIGHT-WIDTH)/6 <= mouse[1] <= WIDTH+(HEIGHT-WIDTH)/2: 
        pygame.draw.rect(gameDisplay,light_grey,[7*WIDTH/10,WIDTH+(HEIGHT-WIDTH)/6,BUTTON_WIDTH,BUTTON_HEIGHT])
    else:
        pygame.draw.rect(gameDisplay,dark_grey,[7*WIDTH/10,WIDTH+(HEIGHT-WIDTH)/6,BUTTON_WIDTH,BUTTON_HEIGHT])
    if 7*WIDTH/10 <= mouse[0] <= 9*WIDTH/10 and WIDTH+4*(HEIGHT-WIDTH)/6 <= mouse[1] <= WIDTH+5*(HEIGHT-WIDTH)/6: 
        pygame.draw.rect(gameDisplay,light_grey,[7*WIDTH/10,WIDTH+4*(HEIGHT-WIDTH)/6,BUTTON_WIDTH,BUTTON_HEIGHT/2])
    else:
        pygame.draw.rect(gameDisplay,dark_grey,[7*WIDTH/10,WIDTH+4*(HEIGHT-WIDTH)/6,BUTTON_WIDTH,BUTTON_HEIGHT/2])
    speed_solve = BUTTON_FONT.render("Speed Solve", True, white)
    speed_solve_width = speed_solve.get_rect().width
    speed_solve_height = speed_solve.get_rect().height
    gameDisplay.blit(speed_solve,(WIDTH/10+(BUTTON_WIDTH-speed_solve_width)/2,WIDTH+(HEIGHT-WIDTH)/6+(BUTTON_HEIGHT-speed_solve_height)/2))
    demo_solve = BUTTON_FONT.render("Demo Solve", True, white)
    demo_solve_width = demo_solve.get_rect().width
    demo_solve_height = demo_solve.get_rect().height
    gameDisplay.blit(demo_solve,(4*WIDTH/10+(BUTTON_WIDTH-demo_solve_width)/2,WIDTH+(HEIGHT-WIDTH)/6+(BUTTON_HEIGHT-demo_solve_height)/2))
    new_board = BUTTON_FONT.render("New Board", True, white)
    new_board_width = new_board.get_rect().width
    new_board_height = new_board.get_rect().height
    gameDisplay.blit(new_board,(7*WIDTH/10+(BUTTON_WIDTH-new_board_width)/2,WIDTH+(HEIGHT-WIDTH)/6+(BUTTON_HEIGHT-new_board_height)/2))
    reset = BUTTON_FONT.render("Reset", True, white)
    reset_width = reset.get_rect().width
    reset_height = reset.get_rect().height
    gameDisplay.blit(reset,(7*WIDTH/10+(BUTTON_WIDTH-reset_width)/2,WIDTH+4*(HEIGHT-WIDTH)/6+(BUTTON_HEIGHT/2-reset_height)/2))

def handleClick():
    mouse = pygame.mouse.get_pos()
    if WIDTH/10 <= mouse[0] <= 3*WIDTH/10 and WIDTH+(HEIGHT-WIDTH)/6 <= mouse[1] <= WIDTH+(HEIGHT-WIDTH)/2: 
        executeSolve(gameDisplay)

    

gameDisplay = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('Sodoku Solver')
clock = pygame.time.Clock()

gameDisplay.fill(white)
drawBoard(gameDisplay)
for a in range(N):
    for b in range(N):
        if board[a][b]!=0:
            addValid(gameDisplay,a,b,board[a][b])
pygame.display.update()

#executeSolve(gameDisplay)

print(WIDTH/7)
print(2*WIDTH/7)
print(WIDTH+(HEIGHT-WIDTH)/3)
print(WIDTH+2*(HEIGHT-WIDTH)/3)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handleClick()
    handleButtons(gameDisplay)
    pygame.display.update()

pygame.quit()
pygame.init()


printBoard()

print("")
    
#if (not solve(gameDisplay, 0, 0)):
#    print("Not Solvable!!")
#else:
#    printBoard()
printBoard()
printOriginal()

