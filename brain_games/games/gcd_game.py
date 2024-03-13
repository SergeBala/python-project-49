import random
from brain_games.constants import RANGE_START, RANGE_END


def find_gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


def get_quest_and_answ_gcd():
    x = random.randint(RANGE_START, RANGE_END)
    y = random.randint(RANGE_START, RANGE_END)
    return str(x) + " " + str(y), find_gcd(x, y)
