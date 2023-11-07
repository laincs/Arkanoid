# 0 value is transparent, 13 have four lives, 9 have infinity lives
levels = []

ColorChar = { "a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11,
             "m": 12, "n": 13, "o":14, "p":15 }

class Level():
    def __init__(self, lvlData):
        self.lvlData = lvlData
        global levels
        levels.append(self)
        

Level([ "kkkkkkkkkkkkk",
        "k  hhhhhhhh k",
        "k  h      h k",
        "k  h fff  h k",
        "k  h      h k",
        "kkkkkkkkkkkkk"])

Level([ "ppppppppppppp",
        "p           p",
        "p   kkkk    p",
        "p  k    k   p",
        "p   kkkk    p",
        "p           p",
        "ppppppppppppp"])

Level([ "ccccccccccccc",
        "c hhhhhhh h c",
        "c ccccccc c c",
        "c c fff c c c",
        "c c ccc c c c",
        "ccccccccccccc"])

Level([ "gggggggggggg",
        "g g gg g g g",
        "g g gg g g g",
        "g gggggg g g",
        "g g gg g g g",
        "g g gg g g g",
        "gggggggggggg"])

Level([ "hhhhhhhhhhhhh",
        "hhh   h   hhh",
        "hh    h    hh",
        "h     h     h",
        "hh         hh",
        "hhh       hhh",
        "hhhhhhhhhhhhh"])

Level([ " pop popopo p",
        "p           p",
        " popo popopo ",
        "          p  ",
        " popopopopop ",
        "p           p"])


Level([ "b b b b b b b",
        "b   b o o o b",
        "b b b b b b b",
        "b o o o b   b",
        "b b b b b b b",
        "b           b"])


Level([ " i iii iii  i",
        "i   ii   ii  ",
        " i  iii iii  i",
        "ii  ii ii  ii",
        " ii iii iii  i"])

Level([ " r r r r r r r",
        " o o o o o o o",
        " y y y y y y y",
        " g g g g g g g",
        " b b b b b b b",
        " o o o o o o o",
        " p p p p p p p"])

Level([ "r r b b r r b",
        " r r r r r r ",
        "b b b b b b b",
        " g g r r g g ",
        "r r r b b r r",
        " r r r r r r ",
        "b b g g g g b"])

Level([ "ffhhffhhhhhhh",
        "fhhhhfhhhhhhh",
        "fhffhfhhhhhhh",
        "iiiiiiiiiiiii",
        "iiiiiiiiiiiii",
        "iiiiiiiiiiiii"])

Level([ "kkkkkkkkkkkkk",
        "kkkkkkkkkkkkk",
        "ffffhfhfhffff",
        "ffhfffffffhff",
        "iiiiiiiiiiiii",
        "nnnnnnnnnnnnn"])