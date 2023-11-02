import pyxel, levels, random, utilities
from data import *

blocks=[]
players=[]
balls = []

class Block():
    def __init__(self, ax, ay, color, OnBallCollisionEvent):
        self.w = 10
        self.h = 4
        self.x = 3 + (ax * (self.w+2))
        self.y = 10 + (ay * (self.h+2))
        self.color = color
        self.life = 5 if color == 13 else 1
        self.OnBallCollisionEvent = OnBallCollisionEvent
        
    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, levels.ColorChar.get(self.color))
        
    def onBallCollision(self):
        global app
        if (self.color != 9):
            if(self.life >1):
                self.life-=1
            else:
                blocks.remove(self)
                self.OnBallCollisionEvent()

class Ball():
    def __init__(self, pinned, color):
        global players
        self.pinned = pinned
        self.color = color
        self.active = True
        if(pinned):
            self.x = -100
            self.y = -100
        else:
            self.x = players[0].x + players[0].w/2 - 1
            self.y = players[0].y - players[0].h
        self.r = 1
        self.dirX = ((random.randint(0, 1)*2)-1)*(random.random()*2-1)
        self.dirY = (-1)*2
        
    def draw(self):
        pyxel.circ(self.x,self.y,self.r,self.color) #7 white
        if(self.pinned):
            self.x = players[0].x + players[0].w/2 - 1
            self.y = players[0].y - players[0].h
        else:
            self.x += self.dirX 
            self.y += self.dirY 
        self.colliders()
        
    def throwBall(self):
        self.pinned = False
        
    def colliders(self):
        if(self.x <0 or self.x > AppConfig["width"]):
            self.dirX = -self.dirX
            
        if(self.y < 0 ):
            self.dirY = -self.dirY 
        
        if(self.y > AppConfig["height"]):
            global balls
            balls.remove(self)
            
        for c in range(0,1):
            if (self.x > players[c].x and self.x < players[c].x+players[c].w):
                if (self.y > players[c].y-players[c].h and self.y < players[c].y+players[c].h ):
                    self.dirX = self.getDir()
                    self.dirY = -( self.dirY )
        
            for b in blocks:
                if(self.x > b.x and self.x < b.x+b.w):
                    if(self.y > b.y and self.y < b.y + b.h):
                        if(self.x < b.x+1 or self.x > b.x+b.w-1):
                            self.dirX = -( self.dirX )
                        else:
                            self.dirY = -( self.dirY )
                        b.onBallCollision()
                    
    def getDir(self):
        value = (((utilities.Math.clamp(players[0].x - self.x,-players[0].w,0)) + (players[0].w/2))/(-players[0].w/2))*2
        return value
            
class Player():
    def __init__( self, x):
        self.x = x
        self.y = AppConfig["height"] - 20
        self.speed = 2
        self.w = 15
        self.h = 2
        
    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, 7)