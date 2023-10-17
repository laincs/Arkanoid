import pyxel

class Ball():
    def __init__(self):
        self.x = 80
        self.y = 60
        self.r = 1
        self.dirX = -1
        self.dirY = -1
        
    def draw(self):
        pyxel.circ(self.x,self.y,self.r,7)
        self.x += self.dirX
        self.y += self.dirY
        self.colliders()
        
    def colliders(self):
        if(self.x <0 or self.x > 160):
            self.x = 80
            self.y = 60
            self.dirX = 1
            
        if(self.y < 0 or self.y > 120):
            self.dirY = -self.dirY 
            
        for c in range(0,2):
            if (self.x > players[c].x-players[c].w and self.x < players[c].x+players[c].w):
                if (self.y > players[c].y-players[c].h and self.y < players[c].y+players[c].h ):
                    self.dirX = -self.dirX 
                    self.dirX+=(1 * (self.dirX>0))
            
        

class Player():
    def __init__( self, x):
        self.x = x
        self.y = 80
        self.speed = 2
        self.w = 2
        self.h = 15
        
    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, 7)

class App():
    def __init__(self):
        players.append( Player(20))
        players.append( Player(160 - 20))
        pyxel.init(160, 120)
        self.x = 0
        pyxel.run(self.update, self.draw)
        

    def update(self):
        if (pyxel.btn(pyxel.KEY_W)):
            players[0].y-=players[0].speed
        if (pyxel.btn(pyxel.KEY_S)):
            players[0].y+=players[0].speed
            
        if (pyxel.btn(pyxel.KEY_UP)):
            players[1].y-=players[1].speed
        if (pyxel.btn(pyxel.KEY_DOWN)):
            players[1].y+=players[1].speed

    def draw(self):
        pyxel.cls(0)
        for c in players:
            c.draw()
        ball.draw()
        
players=[]
ball = Ball()
app = App()