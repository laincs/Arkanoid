import pyxel, random
import levels

AppConfig = {
  "width": 160,
  "height": 120
}

ColorChar = { "a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11 }

class Math():
    def clamp(n, min, max): 
        if n < min: 
            return min
        elif n > max: 
            return max
        else: 
            return n 

class Block():
    def __init__(self, ax, ay, color):
        self.w = 10
        self.h = 4
        self.x = 3 + (ax * (self.w+2))
        self.y = 3 + (ay * (self.h+2))
        self.color = color
        
    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, ColorChar.get(self.color))

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
            App.ballDestroy()
            
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
                        blocks.remove(b)
                    
    def getDir(self):
        value = (((Math.clamp(players[0].x - self.x,-players[0].w,0)) + (players[0].w/2))/(-players[0].w/2))*2
        print(value)
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

class App():
    def __init__(self):
        self.awake()
        pyxel.init(AppConfig["width"], AppConfig["height"])
        pyxel.run(self.update, self.draw)
        
    def awake(self):
        players.append( Player(AppConfig["width"]/2))
        for c in range(0,10):
            balls.append( Ball(False, random.randint(1,12)))
        self.buildLvl(levels.level1)
    
    def buildLvl(self, lvl):
        print(lvl.lvlData[0][0])
        for y in range (0, len(lvl.lvlData)):
            ax = 0
            for c in lvl.lvlData[y]:
                if(c != "_"): blocks.append( Block(ax, y, c) )
                ax+=1

    def update(self):
        autoPlay = True
        offset = 3
        if(autoPlay):
            if(balls[0].x > players[0].x + (players[0].w/2) -offset):
                players[0].x+=2
            if(balls[0].x < players[0].x + (players[0].w/2) +offset):
                players[0].x-=2
        
        
        if (pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT)):
            players[0].x-=players[0].speed
        if (pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT)):
            players[0].x+=players[0].speed
        """ if (pyxel.btn(pyxel.KEY_SPACE) or pyxel.btn(pyxel.KEY_UP)):
            ball.throwBall() """

    def draw(self):
        pyxel.cls(0)
        for c in players:
            c.draw()
        for c in blocks:
            c.draw()
        for c in balls:
            c.draw()
        
    def ballDestroy():
        global balls
        for c in range(0,10):
            if(len(balls)<2000):
                print(len(balls))
                balls.append( Ball(False, random.randint(1,12)))
        
blocks=[]
players=[]
balls = []
app = App()