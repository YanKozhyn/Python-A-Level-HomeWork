"""This module for custom exceptions"""


class EnemyDown(Exception):
    """ Custom exception when enemy down"""
    def __str__(self):
        return 'Enemy down'


class GameOver(Exception):
    """ Custom exception when game is over"""
    def __str__(self):
        return 'Game over'
