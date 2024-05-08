import pygame
import time
from pygame.math import Vector2
import random
A = 0
D = 1
W = 2
S = 3
SPACE = 4
E = 7



Guy = pygame.image.load('GuySS2.png') #load your spritesheet
Guy.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)
expansion2 = pygame.image.load('malevolent_shrine.png')

sparks = pygame.image.load('Blackflash.png')

expansion = pygame.image.load('domain.png')

class player():
    def __init__ (self):
        #player variables
        self.pos = Vector2(200,615)
        self.vx = 0
        self.vy = 0
        self.frameWidth = 95
        self.frameHeight = 95
        self.RowNum = 0 #for left animation, this will need to change for other animations
        self.frameNum = 1
        self.ticker = 0
        self.direction = D
        self.HP = 1000
        self.last = pygame.time.get_ticks()
        self.cooldown = 1500
        self.blackflash = False
        self.sparkX = self.pos.x
        self.sparkY = self.pos.y - 30
        self.Ryoki_Tenkai = False
        self.CD = 0
        self.isOnCooldown = False
        self.cooldown_duration = 5
        self.last_used_time = 0

    def move(self, keys, map):
        #LEFT MOVEMENT
        if keys[A] == True:
            self.vx = -3
            self.RowNum = 0
            self.direction = A
        #RIGHT MOVEMENT
        elif keys[D] == True:
            self.vx = 3
            self.RowNum = 3
            self.direction = D
        #TURN OFF X VELOCITY
        else:
            self.vx = 0
        
        if keys[W] == True:
            self.vy = -3
            self.RowNum = 1
            self.direction = W
        elif keys[S] == True:
            self.vy = 3
            self.RowNum = 2
            self.direction = S
        else:
            self.vy = 0
        
        if self.vx<0 or self.vx>0 or self.vy <0 or self.vy>0: #left animation
        # Ticker is a spedometer. We don't want Chicken animating as fast as the
        # processor can process! Update Animation Frame each time ticker goes over
            self.ticker+=1
        
        if self.ticker%10==0: #only change frames every 10 ticks
          self.frameNum+=1
           #If we are over the number of frames in our sprite, reset to 0.
           #In this particular case, there are 8 frames (0 through 7)
        if self.frameNum>7: 
           self.frameNum = 0
           
        
        

        #COLLISION
        #LEFT
        if map [int((self.pos.y-10) / 50)][int((self.pos.x - 10) / 50)] == 2:
            self.pos.x+=3
        #RIGHT
        if map [int((self.pos.y) / 50)][int((self.pos.x +30 + 5) / 50)] == 2:
            self.pos.x-=3
        #DOWN
        if map [int((self.pos.y + 30 + 5) / 50)][int((self.pos.x ) / 50)] == 2:
            self.pos.y-=3
        #UP
        if map [int((self.pos.y - 20) / 50)][int((self.pos.x) / 50)] == 2:
            self.pos.y+=3

        self.pos.y+=self.vy
        self.pos.x+=self.vx

    def PlayerHp(self, eXpos, eYpos):
        now = pygame.time.get_ticks()
        if eXpos + 20 > self.pos.x and eXpos < self.pos.x + 50 and eYpos + 20 > self.pos.y and eYpos < self.pos.y + 50:
            if now - self.last >= self.cooldown:
                self.last = now
                self.HP -= 100
    
    def RCT(self, uses):
        #print(self.HP)
        self.HP = 1000
        uses -= 1

    def Blackflash(self, screen):
        chance = random.randrange(1, 11)
        if chance == 1:
            self.blackflash = True
            if self.blackflash == True:
                screen.blit(sparks, (self.pos.x, self.pos.y - 30) )
        else:
            print("improve your focus")
        
    #def Bcollision(self, ExPos, EyPos):
        #if 
        


class Gojo(player):
    def __init__(self):
        player.__init__(self)


    def draw(self, screen):
        #pygame.draw.rect(screen, (255,0,255), (self.pos.x, self.pos.y, 30, 30))
        screen.blit(Guy, (self.pos.x-40, self.pos.y -40), (self.frameWidth*self.frameNum, self.RowNum*self.frameHeight, self.frameWidth, self.frameHeight))

    def domain(self, screen):
        screen.blit(expansion, (0,0), (0,0, 10000, 10000))
        self.Ryoki_Tenkai = True
        self.CD -= 1000
    
    def PlayerHp(self, eXpos, eYpos):
        player.PlayerHp(self, eXpos, eYpos)
    
    def RCT(self, uses):
        player.RCT(self, uses = 5)
    
    def Blackflash(self, screen):
        player.Blackflash(self, screen)
    

    


class Sukuna(player):
    def __init__ (self):
        player.__init__(self)

    def draw(self, screen):
        #pygame.draw.rect(screen, (255,0,255), (self.pos2.x, self.ypos2, 30, 30))
        screen.blit(Guy, (self.pos.x-40, self.pos.y -40), (self.frameWidth*self.frameNum, self.RowNum*self.frameHeight, self.frameWidth, self.frameHeight))

    def domain(self, screen):
        screen.blit(expansion2, (0,0), (0,0, 10000, 10000))

      # current_time = time.time()

      # if current_time - self.last_used_time >= self.cooldown_duration:
      #     print("cd started")
      #     self.last_used_time = current_time
      # else:
      #     print("move is on cd")
      # self.isOnCooldown = True
      # self.Ryoki_Tenkai = True
      # self.CD += 50000
      # while self.isOnCooldown == True:
      #     self.CD -= 10
      #     if self.CD <= 0:
      #         self.isOnCooldown = False
              


    def move(self, keys, map):
        player.move(self, keys, map)

    def PlayerHp(self, eXpos, eYpos):
        player.PlayerHp(self, eXpos, eYpos)

    def Blackflash(self, screen):
        player.Blackflash(self, screen)
    
    def RCT(self, uses):
        player.RCT(self, uses = 5)
    