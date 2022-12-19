""" It's module for GLOBAL SETTINGS"""
from enum import IntEnum

INITIAL_PLAYER_HEALTH = 5
SCORE = 0
ENEMY_LEVEL = 1
result_of_fight = ["Draw", "Victory", "Defeat"]


class Heroes(IntEnum):
    """ Enum for our heroes """
    WARRIOR = 1
    ROBBER = 2
    WIZARD = 3
