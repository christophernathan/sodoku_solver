import pygame
from src.utils.draw import *
from src.utils.game import *

def playGame(): # main game loop
    pygame.init()
    gameDisplay = pygame.display.set_mode([WIDTH,HEIGHT])
    pygame.display.set_caption('Sudoku Solver')
    resetBoard(gameDisplay)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handleClick(gameDisplay)
        drawButtons(gameDisplay)
        pygame.display.update()
    pygame.quit()

playGame()