import pyxel, random

AppConfig = {
  "width": 160,
  "height": 120
}

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
        self.x = 50
        self.y = 50
        self.color = color
        
    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, self.color)

class Ball():
    def __init__(self):
        self.pinned = True
        self.x = -100
        self.y = -100
        self.r = 1
        self.dirX = ((random.randint(0, 1)*2)-1)*2
        self.dirY = (-1)*2
        
    def draw(self):
        pyxel.circ(self.x,self.y,self.r,7)
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
            App.ballDestroy()
            
        for c in range(0,1):
            if (self.x > players[c].x-players[c].w and self.x < players[c].x+players[c].w):
                if (self.y > players[c].y-players[c].h and self.y < players[c].y+players[c].h ):
                    self.dirX = self.getDir()
                    self.dirY = -( self.dirY )
                    
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
        blocks.append( Block(50,50, 12) )
        players.append( Player(AppConfig["width"]/2))
        pyxel.init(AppConfig["width"], AppConfig["height"])
        pyxel.run(self.update, self.draw)
        

    def update(self):
        if (pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT)):
            players[0].x-=players[0].speed
        if (pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT)):
            players[0].x+=players[0].speed
        if (pyxel.btn(pyxel.KEY_SPACE) or pyxel.btn(pyxel.KEY_UP)):
            ball.throwBall()

    def draw(self):
        pyxel.cls(0)
        for c in players:
            c.draw()
        for c in blocks:
            c.draw()
        ball.draw()
        
    def ballDestroy():
        global ball
        ball = Ball()
        
blocks=[]
players=[]
ball = Ball()
app = App()