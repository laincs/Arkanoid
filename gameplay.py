from turtle import speed
import pyxel, levels, random, utilities
from data import *

blocks = []
players = []
balls = []

class Block():
    def __init__(self, ax, ay, color, OnBallCollisionEvent):
        self.w = 16
        self.h = 8
        self.x = 3 + (ax * (self.w+2))
        self.y = 10 + (ay * (self.h+2))
        self.color = color
        self.life = 5 if color == "n" else 1
        self.OnBallCollisionEvent = OnBallCollisionEvent
        
    def draw(self):
        pyxel.rect(self.x+2, self.y+2, self.w, self.h, 0)
        pyxel.rect(self.x, self.y, self.w, self.h, levels.ColorChar.get(self.color))
        
    def onBallCollision(self):
        global app
        if (self.color != "j"):
            #print(f"{self.color} - {self.life}")
            if(self.life >1):
                self.life-=1
            else:
                blocks.remove(self)
                self.OnBallCollisionEvent()

class Ball():
    def __init__(self, pinned, color, OnBallLost):
        global players
        self.pinned = pinned
        self.color = color
        self.active = True
        self.OnBallLost = OnBallLost
        if(pinned):
            self.x = -100
            self.y = -100
        else:
            self.x = players[0].x + players[0].w/2 - 1
            self.y = players[0].y - players[0].h
        self.r = 2
        self.speed = 1
        self.dirX = ((random.randint(0, 1)*2)-1)*(random.random()*2-1)
        self.dirY = (-1)*2
        
    def draw(self):
        pyxel.circ(self.x+2,self.y+2,self.r,0)
        pyxel.circ(self.x,self.y,self.r,self.color) #7 white
        
        if(self.pinned):
            self.x = players[0].x + players[0].w/2 - 1
            self.y = players[0].y - players[0].h
        else:
            self.x += (self.dirX * self.speed)
            self.y += (self.dirY * self.speed)
        self.colliders()
        
        
        
    def throwBall(self):
        self.pinned = False
        
    def colliders(self):
        if(self.x <4 or self.x > AppConfig["width"]-4):
            self.dirX = -self.dirX
            
        if(self.y < 12 ):
            self.dirY = -self.dirY 
        
        if(self.y > AppConfig["height"]):
            self.OnBallLost()
            global balls
            balls.remove(self)
            
        for c in range(0,1):
            if (self.x+self.r > players[c].x and self.x-self.r < players[c].x+players[c].w):
                if (self.y > players[c].y-players[c].h and self.y < players[c].y+players[c].h ):
                    self.dirX = self.getDir()
                    self.dirY = -( self.dirY )
        
            for b in blocks:
                if(self.x+self.r > b.x and self.x-self.r < b.x+b.w):
                    if(self.y+self.r > b.y and self.y-self.r < b.y + b.h):
                        if(self.x+self.r < b.x+1 or self.x-self.r > b.x+b.w-1):
                            self.dirX = -( self.dirX )
                        else:
                            self.dirY = -( self.dirY )
                        b.onBallCollision()
                    
    def getDir(self):
        value = (((utilities.Math.clamp(players[0].x - self.x,-players[0].w,0)) + (players[0].w/2))/(-players[0].w/2))*2
        if(value>0):
            value = utilities.Math.clamp(value, 0.3, 10)
        else:
            value = utilities.Math.clamp(value, -10, -0.3)
        #print(value)
        return value
            
class Player():
    def __init__( self, x):
        self.x = x
        self.y = AppConfig["height"] - 20
        self.speed = 2
        self.w = 30
        self.h = 5
        
    def draw(self):
        pyxel.rect(self.x+2, self.y+2, self.w, self.h, 0)
        pyxel.rect(self.x, self.y, self.w, self.h, 7)