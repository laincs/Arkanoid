import pyxel
from gameplay import *
from data import *
from hud import *
from scenes import *


class App():
    def __init__(self):
        self.curScene = StartScene(self.GoGameScene)
        self.start()
        pyxel.init(AppConfig["width"], AppConfig["height"])
        pyxel.run(self.update, self.draw)
        
    def start(self):
        self.curScene.start()
    
    def update(self):
        self.curScene.update()
    
    def draw(self):
        self.curScene.draw()
        
    def GoGameScene(self):
        self.curScene = GameScene()
        self.curScene.start()
        
    


app = App()