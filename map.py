import pygame

brick = pygame.image.load('brick.png')
dirt = pygame.image.load('dirt.png')
lava = pygame.image.load('lava.png')

def MapF (screen, map):
    for i in range(20):
        for j in range(20):
            if map[i][j] == 1:
                screen.blit(dirt, (j*50, i * 50), (0, 0, 50, 50))
            if map[i][j] == 2:
                screen.blit(brick, (j *50, i * 50), (0, 0, 50, 50))
            if map[i][j] == 3:
                screen.blit(lava, (j *50, i * 50), (0, 0, 50, 50))