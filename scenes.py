import pyxel, random
import levels, utilities
from gameplay import *
from data import *
from hud import *

class StartScene():
    def __init__(self, triggerEvent):
        self.triggerEvent = triggerEvent
    
    def start(self):
        Data["Lives"] = 3
        Data["Score"] = 0
    
    def update(self):
        if (pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_KP_ENTER)):
            self.triggerEvent()
    
    def draw(self):
        pyxel.text(AppConfig["width"]/2-40, (AppConfig["height"]/2)-20, f"Pelota Ladrillo Rompe", 7)
        pyxel.text(AppConfig["width"]/2-25, (AppConfig["height"]/2-10), f"Juego Colores", 9)
        pyxel.text(AppConfig["width"]/2-40, (AppConfig["height"]/2+50), f"Press SPACE to start", 9)
        pyxel.text(AppConfig["width"]/2+75, (AppConfig["height"]/2+110), f"Made by Lian", 7)
        hudMan.update()
        #pyxel.blt(50, 50, 0, 0, 0, 10, 10, 0)
        
class LoadScene():
    def __init__(self, triggerEvent):
        self.triggerEvent = triggerEvent
        self.time = 0
    
    def start(self):
        pass
    
    def update(self):
        self.time += 1
        self.time %= 50
        
        if(self.time == (49)):
            self.triggerEvent()
    
    def draw(self):
        lvln = Data["Level"]
        pyxel.text(AppConfig["width"]/2-40, (AppConfig["height"]/2)-20, f"Level {lvln+1}", 7)
        hudMan.update()
        #pyxel.blt(50, 50, 0, 0, 0, 10, 10, 0)

class GameScene():
    def __init__(self, triggerLvl, triggerEvent):
        self.time = 0
        self.lvl = Data["Level"]
        self.triggerLvl = triggerLvl
        self.triggerEvent = triggerEvent
        self.offset = [0,0]
    
    def start(self):
        if(len(players)<=0): players.append( Player(AppConfig["width"]/2))
        global balls
        balls.append( Ball(True, 7, self.onBallLost))
        self.buildLvl(levels.levels[self.lvl])
    
    def goNextLvl(self):
        Data["Level"]+=1
        balls.clear()
        self.triggerLvl()
        
    def onBallLost(self):
        Data["Lives"]-=1
        if(Data["Lives"]>0):
            balls.append( Ball(True, 7, self.onBallLost))
        else:
            self.triggerEvent()
        
        
    def onTriggerBallDestroy(self):
        hudMan.increaseScore(100)
        self.checkEmptyLevel()
        
    def checkEmptyLevel(self):
        if(len(blocks) == 0):
            self.goNextLvl()
        else:
            aux= 0
            for c in blocks:
                if(c.color != 13):
                    aux+=1
            
            #print(f"left: {aux}")
            if(aux<=0):
                self.goNextLvl()
                   
    def buildLvl(self, lvl):
        #print(lvl.lvlData[0][0])
        global blocks
        blocks.clear()
        for y in range (0, len(lvl.lvlData)):
            ax = 0
            for c in lvl.lvlData[y]:
                if(c != "_" and c!=" "): blocks.append( Block(ax, y+1, c, self.onTriggerBallDestroy) )
                ax+=1

    def update(self):
        autoPlay = False
        offset = 3
        if(autoPlay):
            if(balls[0].x > players[0].x + (players[0].w/2) -offset):
                players[0].x+=2
            if(balls[0].x < players[0].x + (players[0].w/2) +offset):
                players[0].x-=2
        
        if (pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT)) and (players[0].x > 3):
            players[0].x-=players[0].speed
        if (pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT)) and (players[0].x < data.AppConfig["width"]- 3 - players[0].w):
            players[0].x+=players[0].speed
        if (pyxel.btnp(pyxel.KEY_W) or pyxel.btnp(pyxel.KEY_SPACE)):
            for ball in balls: ball.throwBall()
            
        self.time += 1
        self.time %= 300
        
        if(self.time == (29*10)):
            Data["Score"]-=10
        
    def drawBg(self):
        speed=.5
        self.offset[0]+=speed
        self.offset[1]+=speed
        if(self.offset[0]>=20):
            self.offset[0]=0
            self.offset[1]=0
        for x in range(-1, 15):
            for y in range(-1,15):
                posX = x * 20
                posY = y * 20
                pyxel.circ(posX + self.offset[0], posY+self.offset[1], 10, 1)
                
        #mask
        pyxel.rect(0, 0, data.AppConfig["width"], 10, 0)
        pyxel.rect(0, 0, 3, data.AppConfig["height"], 0)
        pyxel.rect(data.AppConfig["width"]-3, 0, 3, data.AppConfig["height"], 0)
        
    def drawFrame(self):
        
        
        #frame
        pyxel.line(0, 8, data.AppConfig["width"], 8, 7)
        pyxel.line(0, 10, data.AppConfig["width"], 10, 7)
        pyxel.line(0, 8, 0, data.AppConfig["height"], 7)
        pyxel.line(2, 8, 2, data.AppConfig["height"], 7)
        pyxel.line(data.AppConfig["width"]-1, 8, data.AppConfig["width"]-1, data.AppConfig["height"], 7)
        pyxel.line(data.AppConfig["width"]-3, 8, data.AppConfig["width"]-3, data.AppConfig["height"], 7)

    def draw(self):
        pyxel.cls(0)
        self.drawBg()
        hudMan.update()
        for c in players:
            c.draw()
        for c in blocks:
            c.draw()
        for c in balls:
            c.draw()
        self.drawFrame()
            
class EndScene():
    def __init__(self, triggerEvent):
        self.triggerEvent = triggerEvent
    
    def start(self):
        pass
    
    def update(self):
        if (pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_KP_ENTER)):
            self.triggerEvent()
    
    def draw(self):
        pyxel.text(AppConfig["width"]/2-40, (AppConfig["height"]/2)-10, f"Dead End", 7)
        hudMan.update()

hudMan = HUDManager()