#! /usr/bin/python
import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
squareWidth = 200
scoreHeight = 50
DISPLAYSURF = pygame.display.set_mode((3*squareWidth, 3*squareWidth + scoreHeight), 0, 32)
pygame.display.set_caption('TicTacToe')
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
curentPlayer = "X"
xColor = RED
oColor = BLUE
board = [[0,0,0],[0,0,0],[0,0,0]]
DISPLAYSURF.fill(WHITE)
winner = None

pygame.draw.line(DISPLAYSURF, BLACK, (0, squareWidth), (3*squareWidth, squareWidth), 5)
pygame.draw.line(DISPLAYSURF, BLACK, (0, 2*squareWidth), (3*squareWidth, 2*squareWidth), 5)
pygame.draw.line(DISPLAYSURF, BLACK, (squareWidth, 0), (squareWidth, 3*squareWidth), 5)
pygame.draw.line(DISPLAYSURF, BLACK, (2*squareWidth, 0), (2*squareWidth, 3*squareWidth), 5)

while True:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[0] < squareWidth:
                x = 0
            elif pos[0] < 2*squareWidth:
                x = 1
            else:
                x = 2
            if pos[1] < squareWidth:
                y = 0
            elif pos[1] < 2*squareWidth:
                y = 1
            else:
                y = 2
            if not(board[x][y]):
                if curentPlayer == "X":
                    board[x][y] = 1
                    lastAction = pygame.draw.line(DISPLAYSURF, xColor, (x*squareWidth + squareWidth, y*squareWidth + squareWidth), (x* squareWidth, y*squareWidth), 5)
                    lastAction2 = pygame.draw.line(DISPLAYSURF, xColor, (x* squareWidth, y * squareWidth + squareWidth), (x* squareWidth + squareWidth, y* squareWidth), 5)
                    curentPlayer = "O"
                else:
                    board[x][y] = 5
                    lastAction = pygame.draw.circle(DISPLAYSURF, oColor, (int(x*squareWidth+squareWidth/2),int(y*squareWidth+squareWidth/2)), int(squareWidth/2), 5)
                    lastAction2 = None
                    curentPlayer = "X"
                transBoard = [list(x) for x  in zip(*board)]
                print(board)
                print(transBoard)
                for i in range(3):
                    if sum(board[i]) == 3 or sum(transBoard[i]) == 3:
                        winner = "X"
                    elif sum(board[i]) == 15 or sum(transBoard[i]) == 15:
                        winner = "O"
                if board[1][1]:
                    if board[1][1] == board[0][0] and board[1][1] == board[2][2]:
                        if board[1][1] == 1:
                            winner = "X"
                        else:
                            winner = "O"
                    if board[1][1] == board[0][2] and board[1][1] == board[2][0]:
                        if board[1][1] == 1:
                            winner = "X"
                        else:
                            winner = "O"
                if winner:
                     fontObj = pygame.font.Font('freesansbold.ttf', 32)
                     pygame.draw.line(DISPLAYSURF, WHITE,(0, squareWidth * 3 + scoreHeight/2),(squareWidth * 3, squareWidth * 3 + scoreHeight/2), scoreHeight)
                     textSurfaceObj = fontObj.render("{} wins".format(winner), True, BLACK,)
                     textRectObj = textSurfaceObj.get_rect()
                     textRectObj.center = (55 ,squareWidth * 3 + scoreHeight/2)
                     DISPLAYSURF.blit(textSurfaceObj, textRectObj)
                     textSurfaceObj2 = fontObj.render("Press space for new game", True, BLACK,)
                     textRectObj2 = textSurfaceObj2.get_rect()
                     textRectObj2.center = (squareWidth * 3 - 210,squareWidth * 3 + scoreHeight/2)
                     DISPLAYSURF.blit(textSurfaceObj2, textRectObj2)
                     print ("%s WINS"%(winner))

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                DISPLAYSURF.fill(WHITE)
                pygame.draw.line(DISPLAYSURF, BLACK, (0, squareWidth), (3*squareWidth, squareWidth), 5)
                pygame.draw.line(DISPLAYSURF, BLACK, (0, 2*squareWidth), (3*squareWidth, 2*squareWidth), 5)
                pygame.draw.line(DISPLAYSURF, BLACK, (squareWidth, 0), (squareWidth, 3*squareWidth), 5)
                pygame.draw.line(DISPLAYSURF, BLACK, (2*squareWidth, 0), (2*squareWidth, 3*squareWidth), 5)
                winner = None
                curentPlayer = "X"
                board = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
        if not winner:
            fontObj3 = pygame.font.Font('freesansbold.ttf', 32)
            pygame.draw.line(DISPLAYSURF, WHITE,(0, squareWidth * 3 + scoreHeight/2),(squareWidth * 3 , squareWidth * 3 + scoreHeight/2), scoreHeight)
            textSurfaceObj3 = fontObj3.render("{} turn".format(curentPlayer), True, BLACK,)
            textRectObj3 = textSurfaceObj3.get_rect()
            textRectObj3.center = (55 ,squareWidth * 3 + scoreHeight/2)
            DISPLAYSURF.blit(textSurfaceObj3, textRectObj3)
                    
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()