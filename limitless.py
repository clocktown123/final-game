import pygame
import math
import random
from pygame.math import Vector2

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4
W = 5

class fireball:
    def __init__(self):
        self.pos = Vector2(-10,-10)
        self.isAlive = False
        self.direction = RIGHT

    def shoot(self, x, y, dir):
        self.pos.x = x + 20 # start fireball at center of player
        self.pos.y = y +20
        self.isAlive = True
        self.direction = dir

       

    def move(self, dir):
        if self.direction == RIGHT:
            self.pos.x+=20
        elif self.direction == LEFT:
            self.pos.x-=20
        if self.direction == DOWN:
            self.pos.y+=20
        elif self.direction == UP:
            self.pos.y-=20
        
    def draw(self,screen):
        self.rando = random.randrange(0, 2)
        self.redAlive = False
        self.blueAlive = False
        if self.rando == 0:
            self.redAlive = True
        else:
            self.blueAlive = True
        if self.redAlive:
            pygame.draw.circle(screen, (220,20,60), (self.pos.x, self.pos.y), 10)
            pygame.draw.circle(screen, (250,0,0), (self.pos.x, self.pos.y), 5)
        if self.blueAlive:
            pygame.draw.circle(screen, (0,0,225), (self.pos.x, self.pos.y), 10)
            pygame.draw.circle(screen, (65,105,255), (self.pos.x, self.pos.y), 5)
    
    def B_draw(self, screen):
        pygame.draw.circle(screen, (138,43,226), (self.pos.x, self.pos.y), 30)
        pygame.draw.circle(screen, (147,112,219), (self.pos.x, self.pos.y), 15)

    def collide(self, x, y):
        if math.sqrt((self.pos.x - x) **2 + (self.pos.y - y) **2) < 25:
            print("collision")
            return True
        else:
            return False
        