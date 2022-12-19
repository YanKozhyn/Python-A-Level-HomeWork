"""main module where our program starts"""
import models
import exceptions


def get_player_name() -> str:
    """method for obtain name of our player"""
    name: str = ''
    while not name:
        name = input('ENTER YOUR NAME: ').strip()
    return name


def play() -> None:
    """method for gathering of all concept of app"""
    player_name = get_player_name()
    player = models.Player(player_name)
    enemy = models.Enemy()
    while True:
        try:
            player.attack(enemy)
            player.defence(enemy)
        except exceptions.EnemyDown as exc:
            print(f"{exc}, your current score = {player.score}")
        except exceptions.GameOver as exc:
            print(f"{exc}, your finally score = {player.score}")
            break


if __name__ == '__main__':
    play()
