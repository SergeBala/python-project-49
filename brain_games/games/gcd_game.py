import brain_games.common_game_logic as gl
from brain_games.games.even_game import get_random_number


def find_gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


def get_quest_and_answ_gcd():
    x = get_random_number()
    y = get_random_number()
    return str(x) + " " + str(y), find_gcd(x, y)


def gcd_game(players_name):
    rules = "Find the greatest common divisor of given numbers."
    gl.play_a_game(players_name, rules, get_quest_and_answ_gcd)
