import pygame
from pygame.locals import *
from sys import exit 
from commons import *

def CheckMouseArea(AreaList, pos):
    for x in range(AreaList):
        x1,y1,x2,y2 = AreaList[x]
        posX,posY = pos
        if (x1 < posX < x2) & (y1 < posY < y2):
            return (x + 1) 
    return 0

def DrawCircleOrSquare():
    print("whatever")

pads = [(0,0,0,0),(1,1,1,1)]
pygame.init()
screen = pygame.display.set_mode()
pygame.display.set_caption("Jogo da velha")
pygame.mouse.set_visible(1)
screen.fill((200, 200, 255))
teta = DisplaySizeX, DisplaySizeY = pygame.display.get_window_size()
print(teta)
#colors
linecolor = (100, 100, 255)
linesize = 10
linemargin = 40




while True : 

    pygame.draw.line(screen, linecolor, (linemargin,DisplaySizeY/3), (DisplaySizeX-(2*linemargin),DisplaySizeY/3), linesize)
    pygame.draw.line(screen, linecolor, (linemargin,DisplaySizeY*2/3), (DisplaySizeX-(2*linemargin),DisplaySizeY*2/3), linesize)
    pygame.draw.line(screen, linecolor, (DisplaySizeX/3,linemargin), (DisplaySizeX/3,DisplaySizeY-(2*linemargin)), linesize)
    pygame.draw.line(screen, linecolor, (DisplaySizeX*2/3,linemargin), (DisplaySizeX*2/3,DisplaySizeY-(2*linemargin)), linesize)
    
    mousePosXY = pygame.mouse.get_pos()
    mouse = pygame.mouse.get_pressed()[0]
    if mouse :
        if CheckMouseArea(pads, mousePosXY) == 1:
            linecolor = (255, 0, 0)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()   