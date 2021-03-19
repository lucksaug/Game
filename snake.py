import pygame, random
from pygame.locals import *
import emoji

clock = pygame.time.Clock()
colision = False
W = 700
H = 600 
UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((700,600))
pygame.display.set_caption(emoji.emojize(':snake: Snake :snake:'))

snake = [(200,200),(210,200),(220,200)]
snake_skin = pygame.Surface((10,10)) #pygame.Surface((h,w)) coloca algo na tela com um tamanho h, w
snake_skin.fill((255,255,255)) # deixa a cobra branca fill((R,G,B))

apple = pygame.Surface((10,10))
apple.fill((255,0,0))
apple_pos = (random.randrange(0,H - 10,10),random.randrange(0,W - 10,10))

my_direction = LEFT

while True:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_RIGHT:
                my_direction = RIGHT
            if event.key == K_LEFT:
                my_direction = LEFT

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    for i in range (len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    screen.fill((0,0,0)) ## limpa a tela
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin, pos)
        if snake [0] == apple_pos:
            snake.append((0,0))
            apple.fill((0,0,0))
            apple_pos = (random.randrange(0,590,10),random.randrange(0,590,10))
            apple.fill((255,0,0))
            screen.blit(apple, apple_pos)

    pygame.display.update()