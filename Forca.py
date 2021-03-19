import pygame
from pygame.locals import *

color1 = (200, 255, 255)
GRAY = (50,50,50)
letra = []
letras_erradas = []
game = True

pygame.init()
tela = pygame.display.set_mode((700,700))
rect1 = (100,100,300,40)

while True:
    tela.fill(WHITE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    rect1 = pygame.draw.rect(tela, GRAY, rect1)
    pygame.display.update()

