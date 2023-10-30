import pyxel, random
import levels, utilities
from gameplay import *
from data import *

class App():
    def __init__(self):
        self.currentLvl = 3
        self.awake()
        pyxel.init(AppConfig["width"], AppConfig["height"])
        pyxel.run(self.update, self.draw)
        
    def awake(self):
        players.append( Player(AppConfig["width"]/2))
        for c in range(0,1):
            balls.append( Ball(False, random.randint(1,12)))
        self.buildLvl(levels.levels[self.currentLvl])
        
    def goNextLvl(self):
        self.currentLvl+=1
        if(self.currentLvl >= len(levels.levels)):
            self.currentLvl = 0
        self.buildLvl(levels.levels[self.currentLvl])
        
    def checkEmptyLevel(self):
        if(len(blocks) == 0):
            self.goNextLvl()
        
    
    def buildLvl(self, lvl):
        print(lvl.lvlData[0][0])
        for y in range (0, len(lvl.lvlData)):
            ax = 0
            for c in lvl.lvlData[y]:
                if(c != "_" and c!=" "): blocks.append( Block(ax, y, c) )
                ax+=1

    def update(self):
        autoPlay = True
        offset = 3
        if(autoPlay):
            if(balls[0].x > players[0].x + (players[0].w/2) -offset):
                players[0].x+=2
            if(balls[0].x < players[0].x + (players[0].w/2) +offset):
                players[0].x-=2
        
        self.checkEmptyLevel()
        
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

app = App()