import pyxel, random

AppConfig = {
  "width": 160,
  "height": 120
}

class Ball():
    def __init__(self):
        self.x = AppConfig["width"]/2
        self.y = AppConfig["height"]/2
        self.r = 1
        self.dirX = ((random.randint(0, 1)*2)-1)*2
        self.dirY = (-1)*2
        
    def draw(self):
        pyxel.circ(self.x,self.y,self.r,7)
        self.x += self.dirX
        self.y += self.dirY
        self.colliders()
        
    def colliders(self):
        if(self.x <0 or self.x > AppConfig["width"]):
            self.dirX = -self.dirX
            """ 
            self.x = AppConfig["width"]/2
            self.y = AppConfig["height"]/2
            self.dirX = (random.randint(0, 1)*2)-1
            self.dirY = (random.randint(0, 1)*2)-1 """
            
        if(self.y < 0 ):
            self.dirY = -self.dirY 
        
        if(self.y > AppConfig["height"]):
            print("ded")
            
        for c in range(0,1):
            if (self.x > players[c].x-players[c].w and self.x < players[c].x+players[c].w):
                if (self.y > players[c].y-players[c].h and self.y < players[c].y+players[c].h ):
                    self.dirY = -self.dirY 
            
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
        players.append( Player(AppConfig["width"]/2))
        pyxel.init(AppConfig["width"], AppConfig["height"])
        pyxel.run(self.update, self.draw)
        

    def update(self):
        if (pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT)):
            players[0].x-=players[0].speed
        if (pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT)):
            players[0].x+=players[0].speed

    def draw(self):
        pyxel.cls(0)
        for c in players:
            c.draw()
        ball.draw()
        
players=[]
ball = Ball()
app = App()