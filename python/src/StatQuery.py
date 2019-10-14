from Player import Player
from enum import Enum

class StatType(Enum):
    RUSH_YDS = 1
    PASS_YDS = 2
    INTERCEPTIONS = 3
    PASS_TDS = 4
    RUSH_TDS = 5
    REC_TDS =  6
    TOT_TDS = 7
    TOT_YDS = 8
    EMPTY = 99

class Stat:
    def __init__(self):
        self.type = StatType.EMPTY
        self.val = 0

    def __init__(self, type, val):
        self.type = type
        self.val = val

class StatQuery:

    def __init__(self):
        self.player = Player()
        self.stat_type = StatType.EMPTY

    def __init__(self, player, stat_type):
        self.player = Player(player)
        self.stat_type = stat_type

    def as_dict(self):
        query = {
            "player": self.player.name,
            "stat": self.stat_type
        }
        return query

    def add_stat(type, val):
        self.stat = Stat(type, val)
