__author__ = 'mih279'

from character import Character


class SideKick(Character):
    def __init__(self, league, name, health, brawl, shoot, dodge, might, finesse, cunning, *abilities):
        Character.__init__(self, league, name, health, brawl, shoot, dodge, might, finesse, cunning, abilities)
