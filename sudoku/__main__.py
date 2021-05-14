import pygame, os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sudoku.utils import draw, game

def playGame(): # main game loop
    pygame.init()
    gameDisplay = pygame.display.set_mode([draw.WIDTH,draw.HEIGHT])
    pygame.display.set_caption('Sudoku Solver')
    game.resetBoard(gameDisplay)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game.handleClick(gameDisplay)
        draw.drawButtons(gameDisplay)
        pygame.display.update()
    pygame.quit()

playGame()