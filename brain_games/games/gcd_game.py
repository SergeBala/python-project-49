from random import randint
from brain_games.constants import RANGE_START, RANGE_END


RULES = "Find the greatest common divisor of given numbers."


def find_gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


def get_quest_and_answ():
    x = randint(RANGE_START, RANGE_END)
    y = randint(RANGE_START, RANGE_END)
    return str(x) + " " + str(y), find_gcd(x, y)
