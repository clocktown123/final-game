import pygame
import random
import math
from pygame.math import Vector2
from limitless import fireball


A = 0
D = 1
W = 2
S = 3

class Enemy:
    def __init__ (self):
        self.pos = Vector2(400,200)
        self.direction = D
        self.isAlive = True
        self.HP = 1000
    
    def die(self, ballx, bally, cleavex, cleavey, hollow, Wslash):
        if math.sqrt((self.pos.x-ballx)**2 + (self.pos.y-bally)**2) <= 0:
            if hollow == True or Wslash == True:
                self.HP -= 200
                if self.HP < 0:
                    self.isAlive = False
            else:
                self.HP -= 100
                if self.HP < 0:
                    self.isAlive = False

                
        if math.sqrt((self.pos.x-cleavex)**2 + (self.pos.y-cleavey)**2) <= 20:
            self.HP -= 100
            if self.HP < 0:
                self.isAlive = False

        print(self.HP)

        
    
    def draw(self, screen):
        if self.isAlive == True:
            pygame.draw.rect(screen, (20, 20, 40), ( self.pos.x, self.pos.y, 20, 20))

    def move(self, map, ticker, px, py):
        if ticker % 40 == 0: #change this number to make him change direction less or more often
            num = random.randrange(0, 4)
            if num == 0:
                self.direction = D
            elif num == 1:
                self.direction = A
            elif num == 2:
                self.direction = W
            elif num == 3:
                self.direction = S
        #check if the player is in the line of sight
        if abs(int(py/50) - int(self.pos.y/50))<2: #check that player and enemy are in the same row
            if px < self.pos.x: #check that player is to the left of the enemy
                self.pos.x -=1
                self.direction = A
            else:
                self.pos.x+=1
                self.direction = D
        if abs(int(px/50) - int(self.pos.x/50))<2:
            if py < self.pos.y: #check that player is to the left of the enemy
                self.pos.y -=1
                self.direction = W
            else:
                self.pos.y+=1
                self.direction = S

       # # Calculate distance between enemy and player
       # dx = px - self.pos.x
       # dy = py - self.pos.y
       # distance = math.sqrt(dx ** 2 + dy ** 2)
#
       # # If player is within a certain distance, track the player
       # if distance < 200:
       #     speed = 1
       #     self.pos.x += dx / distance * speed
       #     self.pos.y += dy / distance * speed
        
        if self.direction == D and map[int((self.pos.y) / 50)][int((self.pos.x + 20) / 50)] == 2:
            self.direction = W
            self.pos.x -= 6
        if self.direction == A and map[int((self.pos.y) / 50)][int((self.pos.x - 20) / 50)] == 2:
            self.direction = S
            self.pos.x += 6
        if self.direction == S and map[int((self.pos.y + 20) / 50)][int((self.pos.x) / 50)] == 2:
            self.direction = A
            self.pos.y -= 6
        if self.direction == W and map[int((self.pos.y - 20) / 50)][int((self.pos.x) / 50)] == 2:
            self.direction = D
            self.pos.y += 6

        if self.direction == D:
            self.pos.x += 3
        elif self.direction == A:
            self.pos.x -= 3
        elif self.direction == W:
            self.pos.y -=3
        elif self.direction == S:
            self.pos.y +=3


class Frog(Enemy):
    def __init__(self):
        Enemy.__init__(self)

    def die(self, ballx, bally, cleavex, cleavey, hollow):
        Enemy.die(self, ballx, bally, cleavex, cleavey, hollow)


    def move(self, map, ticker, px, py):
        Enemy.move(self, map, ticker, px, py)

    def draw(self, screen): #for now
        if self.isAlive == True:
            pygame.draw.rect(screen, (20, 20, 40), ( self.pos.x, self.pos.y, 20, 20))


class Normcurse(Enemy):
    def __init__(self):
        Enemy.__init__(self)

    def die(self, ballx, bally, cleavex, cleavey, hollow):
        Enemy.die(self, ballx, bally, cleavex, cleavey, hollow)


    def move(self, map, ticker, px, py):
        Enemy.move(self, map, ticker, px, py)

    def draw(self, screen): #for now
        if self.isAlive == True:
            pygame.draw.rect(screen, (20, 20, 40), ( self.pos.x, self.pos.y, 20, 20))