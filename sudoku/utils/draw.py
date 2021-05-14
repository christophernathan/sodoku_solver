import pygame
import pygame.freetype

pygame.init()
BOARD_FONT = pygame.font.SysFont("newyork", 50)
BUTTON_FONT = pygame.font.SysFont("newyork", 20)
TIMER_FONT = pygame.font.SysFont("newyork", 60)

WIDTH=600
HEIGHT=800
CELL_WIDTH = (WIDTH-6)/9
BUTTON_WIDTH = WIDTH/5
BUTTON_HEIGHT = (HEIGHT-WIDTH)/3

white = (255,255,255)
black = (0,0,0)
light_grey = (200,200,200)
dark_grey = (100,100,100)
dark_blue = (0,0,150)
light_blue = (100,100,255)
dark_red = (150,0,0)
light_red = (255,100,100)
green = (0,200,0)
dark_green = (0,150,0)
light_green = (100,255,100)
dark_yellow = (155,135,12)
light_yellow = (255,200,24)

def drawRectangle(gameDisplay,color,left,top,width,height,thickness):
    pygame.draw.rect(gameDisplay,color,(left,top,width,height),thickness)

def addValid(gameDisplay,row,col,num): # add number in cell
    text = BOARD_FONT.render(str(num), True, black)
    text_width = text.get_rect().width
    text_height = text.get_rect().height
    gameDisplay.blit(text,(3+col*CELL_WIDTH+((CELL_WIDTH-text_width)/2),3+row*CELL_WIDTH+((CELL_WIDTH-text_height)/2)))
    pygame.display.update()

def removeInvalid(gameDisplay,row,col): # remove number from cell
    drawRectangle(gameDisplay,white,6+col*CELL_WIDTH,6+row*CELL_WIDTH,CELL_WIDTH-6,CELL_WIDTH-6,0)
    pygame.display.update()

def drawInnerBox(gameDisplay,color,row,col,thickness): # outline cell on board
    topOffset=0; leftOffset=0; rightOffset=0; bottomOffset=0
    if row==0:
        topOffset = 2
    if col==0:
        leftOffset = 2
    if row==3 or row==6:
        topOffset = 1
    if col==3 or col==6:
        leftOffset = 1
    if row==2 or row==5 or row==8:
        bottomOffset = 1
    if col==2 or col==5 or col==8:
        rightOffset = 1
    drawRectangle(gameDisplay,color,4+leftOffset+col*CELL_WIDTH,4+topOffset+row*CELL_WIDTH,CELL_WIDTH-1-thickness-leftOffset-rightOffset,CELL_WIDTH-1-thickness-topOffset-bottomOffset,thickness)

def drawBoard(gameDisplay):
    drawRectangle(gameDisplay,black,3,3,WIDTH-6,WIDTH-6,4)
    for a in range(3):
        for b in range(3):
            drawRectangle(gameDisplay,black,3+b*(WIDTH-6)/3,3+a*(WIDTH-6)/3,(WIDTH-6)/3,(WIDTH-6)/3,3)
    for a in range(9):
        for b in range(9):
            drawRectangle(gameDisplay,black,3+b*CELL_WIDTH,3+a*CELL_WIDTH,CELL_WIDTH,CELL_WIDTH,1)

def drawTimer(gameDisplay,startTime):
    currTime = pygame.time.get_ticks() - startTime
    currTime//=10
    currTime/=100
    timer = TIMER_FONT.render(str(currTime),True,dark_blue)
    timer_width = timer.get_rect().width
    timer_height = timer.get_rect().height
    drawRectangle(gameDisplay, white, WIDTH/10, WIDTH+4*(HEIGHT-WIDTH)/6, 2*BUTTON_WIDTH, BUTTON_HEIGHT, 0)
    gameDisplay.blit(timer,(WIDTH/10,WIDTH+4*(HEIGHT-WIDTH)/6))
    pygame.display.update()

def drawComplete(gameDisplay):
    complete = BUTTON_FONT.render("COMPLETE!",True,green)
    gameDisplay.blit(complete,(4*WIDTH/10,WIDTH+4*(HEIGHT-WIDTH)/6))
    pygame.display.update()

def removeComplete(gameDisplay):
    drawRectangle(gameDisplay, white, 4*WIDTH/10, WIDTH+4*(HEIGHT-WIDTH)/6, BUTTON_WIDTH, BUTTON_HEIGHT, 0)
    pygame.display.update()

def drawButtons(gameDisplay):
    mouse = pygame.mouse.get_pos()
    if WIDTH/10 <= mouse[0] <= 3*WIDTH/10 and WIDTH+(HEIGHT-WIDTH)/6 <= mouse[1] <= WIDTH+(HEIGHT-WIDTH)/2: 
        pygame.draw.rect(gameDisplay,light_green,[WIDTH/10,WIDTH+(HEIGHT-WIDTH)/6,BUTTON_WIDTH,BUTTON_HEIGHT])
    else:
        pygame.draw.rect(gameDisplay,dark_green,[WIDTH/10,WIDTH+(HEIGHT-WIDTH)/6,BUTTON_WIDTH,BUTTON_HEIGHT])
    if 4*WIDTH/10 <= mouse[0] <= 6*WIDTH/10 and WIDTH+(HEIGHT-WIDTH)/6 <= mouse[1] <= WIDTH+(HEIGHT-WIDTH)/2: 
        pygame.draw.rect(gameDisplay,light_yellow,[4*WIDTH/10,WIDTH+(HEIGHT-WIDTH)/6,BUTTON_WIDTH,BUTTON_HEIGHT])
    else:
        pygame.draw.rect(gameDisplay,dark_yellow,[4*WIDTH/10,WIDTH+(HEIGHT-WIDTH)/6,BUTTON_WIDTH,BUTTON_HEIGHT])
    if 7*WIDTH/10 <= mouse[0] <= 9*WIDTH/10 and WIDTH+(HEIGHT-WIDTH)/6 <= mouse[1] <= WIDTH+(HEIGHT-WIDTH)/2: 
        pygame.draw.rect(gameDisplay,light_blue,[7*WIDTH/10,WIDTH+(HEIGHT-WIDTH)/6,BUTTON_WIDTH,BUTTON_HEIGHT])
    else:
        pygame.draw.rect(gameDisplay,dark_blue,[7*WIDTH/10,WIDTH+(HEIGHT-WIDTH)/6,BUTTON_WIDTH,BUTTON_HEIGHT])
    if 7*WIDTH/10 <= mouse[0] <= 9*WIDTH/10 and WIDTH+4*(HEIGHT-WIDTH)/6 <= mouse[1] <= WIDTH+5*(HEIGHT-WIDTH)/6: 
        pygame.draw.rect(gameDisplay,light_red,[7*WIDTH/10,WIDTH+4*(HEIGHT-WIDTH)/6,BUTTON_WIDTH,BUTTON_HEIGHT/2])
    else:
        pygame.draw.rect(gameDisplay,dark_red,[7*WIDTH/10,WIDTH+4*(HEIGHT-WIDTH)/6,BUTTON_WIDTH,BUTTON_HEIGHT/2])
    speed_solve = BUTTON_FONT.render("Solve", True, white)
    speed_solve_width = speed_solve.get_rect().width
    speed_solve_height = speed_solve.get_rect().height
    gameDisplay.blit(speed_solve,(WIDTH/10+(BUTTON_WIDTH-speed_solve_width)/2,WIDTH+(HEIGHT-WIDTH)/6+(BUTTON_HEIGHT-speed_solve_height)/2))
    demo_solve = BUTTON_FONT.render("Check", True, white)
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