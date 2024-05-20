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
slash2 = pygame.image.load('cleave_left.png')
slash3 = pygame.image.load('cleave_up.png')
slash4 = pygame.image.load('cleave_down.png')

WCS = pygame.image.load('world_cut.png')
WCS2 = pygame.image.load('world_cut_left.png')
WCS3 = pygame.image.load('world_cut_up.png')
WCS4 = pygame.image.load('world_cut_down.png')

class Cleave:
    def __init__(self):
        self.pos = Vector2(-10,-10)
        self.isAlive = False
        self.direction = D
        self.Wslash  = False

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
        if self.direction == D:
            screen.blit(slash, (self.pos.x, self.pos.y))#screen.blit(slash, (self.pos.x, self.pos.y))
        if self.direction == A:
            screen.blit(slash2, (self.pos.x, self.pos.y))#screen.blit(slash, (self.pos.x, self.pos.y))
        if self.direction == W:
            screen.blit(slash3, (self.pos.x, self.pos.y))#screen.blit(slash, (self.pos.x, self.pos.y))
        if self.direction == S:
            screen.blit(slash4, (self.pos.x, self.pos.y))#screen.blit(slash, (self.pos.x, self.pos.y))
    
    def Wdraw(self, screen):
        if self.direction == D:
            screen.blit(WCS, (self.pos.x, self.pos.y))
        if self.direction == A:
            screen.blit(WCS2, (self.pos.x, self.pos.y))#screen.blit(slash, (self.pos.x, self.pos.y))
        if self.direction == W:
            screen.blit(WCS3, (self.pos.x, self.pos.y))#screen.blit(slash, (self.pos.x, self.pos.y))
        if self.direction == S:
            screen.blit(WCS4, (self.pos.x, self.pos.y))#screen.blit(slash, (self.pos.x, self.pos.y))
    

    def collide(self, x, y):
        if self.Wslash == True:
            if math.sqrt((self.pos.x - x) **2 + (self.pos.y - y) **2) < 50:
                print("collision")
                return True
            else:
                return False
        else:
            if math.sqrt((self.pos.x - x) **2 + (self.pos.y - y) **2) < 25:
                print("collision")
                return True
            else:
                return False
        
        
                
        
        
        