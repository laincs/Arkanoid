import pyxel
from gameplay import *
from data import *
from hud import *
from scenes import *


class App():
    def __init__(self):
        self.curScene = StartScene(self.GoLoadScene)
        self.start()
        pyxel.init(AppConfig["width"], AppConfig["height"], fps=60)
        pyxel.load("assets.pyxres")
        pyxel.run(self.update, self.draw)
        
    def start(self):
        self.curScene.start()
     
    def update(self):
        self.curScene.update()
    
    def draw(self):
        pyxel.cls(0)
        self.curScene.draw()
        
    def GoLoadScene(self):
        self.curScene = LoadScene(self.GoGameScene)
        self.start()
        
    def GoGameScene(self):
        self.curScene = GameScene(self.GoLoadScene, self.GoEndScene)
        self.start()
        
    def GoEndScene(self):
        self.curScene = EndScene(self.GoMenuScene)
        self.start()
        
    def GoMenuScene(self):
        self.curScene = StartScene(self.GoGameScene)
        self.start()

if __name__ == "__main__":
    app = App()