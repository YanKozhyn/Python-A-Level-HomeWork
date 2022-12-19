"""this module for 2 models enemy and player"""
from random import choice
from exceptions import EnemyDown, GameOver
from settings import Heroes, INITIAL_PLAYER_HEALTH, ENEMY_LEVEL, SCORE, result_of_fight


class Enemy:
    """class for enemy"""
    def __init__(self):
        self.level = ENEMY_LEVEL
        self.health = self.level

    def decrease_health(self):
        """method for decrease hp of enemy"""
        self.health -= 1
        if self.health == 0:
            self.level += 1
            self.health = self.level
            raise EnemyDown(self.level - 1)


    def select_attack(self):
        """method for random choose a attacker hero for enemy"""
        return choice(list(Heroes))

    def select_defence(self):
        """method for random choose a defender hero for enemy"""
        return choice(list(Heroes))


class Player:
    """class for our player"""
    def __init__(self, name: str):
        self.name = name
        self.health = INITIAL_PLAYER_HEALTH
        self.score = SCORE

    def decrease_health(self):
        """method for decrease hp if player will get hit"""
        self.health -= 1
        if self.health == 0:
            raise GameOver(self.name, self.score)

    def select_attack(self):
        """method for choose type of hero for attack"""
        while True:
            try:
                user_input = input("Enter choice (1 for Warriors , 2 for Robbers, 3 for Wizards): ")
                selection = int(user_input)
                action = Heroes(selection)
                return action
            except ValueError:
                print("Incorrect input. Please enter a number from 1 to 3.")

    def select_defence(self):
        """method for choose type of hero for defence"""
        while True:
            try:
                user_input = input("Enter choice (1 for Warriors , 2 for Robbers, 3 for Wizards): ")
                selection = int(user_input)
                action = Heroes(selection)
                return action
            except ValueError:
                print("Incorrect input. Please enter a number from 1 to 3.")

    @staticmethod
    def fight(player_action, enemy_action):
        """method for retrieve result of fight"""
        if player_action == enemy_action:
            return result_of_fight[0]
        if player_action == Heroes.WARRIOR and enemy_action == Heroes.ROBBER:
            return result_of_fight[1]
        if player_action == Heroes.ROBBER and enemy_action == Heroes.WIZARD:
            return result_of_fight[1]
        if player_action == Heroes.WIZARD and enemy_action == Heroes.WARRIOR:
            return result_of_fight[1]
        return result_of_fight[2]

    def attack(self, enemy: Enemy) -> None:
        """method for attack by player"""
        attack = self.select_attack()
        defence = enemy.select_defence()
        battle_result = self.fight(attack, defence)
        if battle_result == result_of_fight[0]:
            print("IT'S A DRAW!")
        elif battle_result == result_of_fight[1]:
            try:
                enemy.decrease_health()
                self.score += 1
                print("YOUR ATTACK IS SUCCESSFUL!")
            except EnemyDown:
                self.score += 2
                raise
        elif battle_result == result_of_fight[2]:
            print("YOUR ATTACK IS FAILED!")

    def defence(self, enemy: Enemy):
        """method for defence by player"""
        defence = self.select_defence()
        attack = enemy.select_attack()
        battle_result = self.fight(defence, attack)
        if battle_result == result_of_fight[0]:
            print("IT'S A DRAW!")
        elif battle_result == result_of_fight[1]:
            self.decrease_health()
            print("YOUR DEFENCE IS FAILED!")
        elif battle_result == result_of_fight[2]:
            print("YOUR DEFENCE IS SUCCESSFUL!")
