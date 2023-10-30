# 0 value is transparent, 13 have four lives, 9 have infinity lives
levels = []

ColorChar = { "a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11,
             "m": 12, "n": 13, "o":14, "p":15 }

class Level():
    def __init__(self, lvlData):
        self.lvlData = lvlData
        global levels
        levels.append(self)

Level([ "ppppppppppppp",
        "ppppppppppppp",
        "ppppppppppppp",
        "ppppppppppppp",
        "ppppppppppppp",
        "ppppppppppppp",
        "ppppppppppppp",
        "ppppppppppppp",
        "ppppppppppppp"])


Level([ "eeee         ",
        "e  e    ooo  ",
        "e  eppppo  o ",
        "e  e    o   o",
        "eeee    o   o",
        "e  eppppo  o ",
        "e  e    ooo  ",
        "e  e         ",
        "eeee         "])

Level([ "             ",
        "ffffffhhhhhhh",
        "ffhhffhhhhhhh",
        "fhhhhfhhhhhhh",
        "fhffhfhhhhhhh",
        "iiiiiiiiiiiii",
        "iiiiiiiiiiiii",
        "iiiiiiiiiiiii",
        "             "])

Level([ "kkkkkkkkkkkkk",
        "kkkkkkkkkkkkk",
        "kkkkkkkkkkkkk",
        "ffffffhffffff",
        "ffffhfffhffff",
        "ffhfffffffhff",
        "iiiiiiiiiiiii",
        "iiiiiiiiiiiii",
        "iiiiiiiiiiiii"])