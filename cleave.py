import pygame
import math
from pygame.math import Vector2


A = 0
D = 1
W = 2
S = 3
SPACE = 4
F = 5

slash = pygame.image.load('cleave.png')
WCS = pygame.image.load('world_cut.png')

class Cleave:
    def __init__(self):
        self.pos = Vector2(-10,-10)
        self.isAlive = False
        self.direction = D

    def shoot(self, x, y, dir):
        self.pos.x = x + 20 # start fireball at center of player
        self.pos.y = y - 20 
        self.damage = 100
        self.isAlive = True
        self.direction = dir

       

    def move(self, dir):
        if self.direction == D:
            self.pos.x+=20
        elif self.direction == A:
            self.pos.x-=20
        if self.direction == S:
            self.pos.y+=20
        elif self.direction == W:
            self.pos.y-=20
        
    def draw(self,screen):
        screen.blit(slash, (self.pos.x, self.pos.y))#screen.blit(slash, (self.pos.x, self.pos.y))
    
    def Wdraw(self, screen):
        screen.blit(WCS, (self.pos.x, self.pos.y))
    

    def collide(self, x, y):
        if math.sqrt((self.pos.x - x) **2 + (self.pos.y - y) **2) < 25:
            print("collision")
            return True
        else:
            return False
        