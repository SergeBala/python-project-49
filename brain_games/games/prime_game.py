import random
from brain_games.constants import RANGE_START, RANGE_END


def is_prime(nb):
    i = 2
    if nb < 2:
        return "no"
    while i <= (nb // i):
        if nb % i == 0:
            return "no"
        i += 1
    return "yes"


def get_quest_and_answ_prime():
    number = random.randint(RANGE_START, RANGE_END)
    answer = is_prime(number)
    return str(number), answer
