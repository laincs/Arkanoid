import pyxel, data

Data = {"Lives":3, "Score":0}
HUDElements = []

class HUDElement():
    def __init__(self, target, str, x, y, color):
        self.target = target
        self.value = Data.get(target)
        self.str = str
        self.x = x
        self.y = y
        self.color = color
        
    def print(self):
        pyxel.text(self.x, self.y, f"{self.str}{Data.get(self.target)}", self.color)
    
    
class HUDManager():
    def __init__(self):
        HUDElements.append( HUDElement("Lives", "Lives: ", 20, 2, 7) )
        HUDElements.append( HUDElement("Score", "Score: ", data.AppConfig.get("width")-50, 2, 7) )
        
    def increaseScore(self, value):
        Data["Score"]+=value
        
    def update(self):
        for c in HUDElements:
            c.print()