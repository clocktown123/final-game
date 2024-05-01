import pygame

def Health(screen, player):
    if player == 1000:
        pygame.draw.rect(screen, (255, 6, 0), (55, 55, 100, 20))
    elif player == 900:
        pygame.draw.rect(screen, (255, 6, 0), (55, 55, 90, 20))
    elif player == 800:
        pygame.draw.rect(screen, (255, 6, 0), (55, 55, 80, 20))
    elif player == 700:
        pygame.draw.rect(screen, (255, 6, 0), (55, 55, 70, 20))
    elif player == 600:
        pygame.draw.rect(screen, (255, 6, 0), (55, 55, 60, 20))
    elif player == 500:
        pygame.draw.rect(screen, (255, 6, 0), (55, 55, 50, 20))
    elif player == 400:
        pygame.draw.rect(screen, (255, 6, 0), (55, 55, 40, 20))
    elif player == 300:
        pygame.draw.rect(screen, (255, 6, 0), (55, 55, 30, 20))
    elif player == 200:
        pygame.draw.rect(screen, (255, 6, 0), (55, 55, 20, 20))
    elif player == 100:
        pygame.draw.rect(screen, (255, 6, 0), (55, 55, 10, 20))
    elif player == 10:
        pygame.draw.rect(screen, (255, 6, 0), (55, 55, 1, 20))