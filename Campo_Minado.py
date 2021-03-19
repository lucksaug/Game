import pygame
from pygame.locals import *

pygame.init()

H = 600
W = 700

pygame.display.set_mode ((H,W))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    if event.type == MOUSEBUTTONDOWN:
        if event.key