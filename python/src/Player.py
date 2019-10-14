from enum import Enum

class position(Enum):
    QB = 'QB'
    RB = 'RB'
    WR = 'WR'
    DE = 'DE'
    UDF = 'UDF'

class Player:

    def __init__(self):
        self.position = position.UDF
        self.name = 'Zane Dunnings'

    def __init__(self, name):
        self.position = position.UDF
        self.name = name

    def set_position(self, pos):
        for class_pos in position:
            if(pos==class_pos):
                self.position = class_pos

    def set_name(self, name):
        self.name = name
