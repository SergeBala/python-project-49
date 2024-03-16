from random import randint
from brain_games.constants import RANGE_START, RANGE_END


PRIM_RULES = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."


def is_prime(nb):
    i = 2
    if nb < 2:
        return False
    while i <= (nb // i):
        if nb % i == 0:
            return False
        i += 1
    return True


def get_quest_and_answ_prime():
    number = randint(RANGE_START, RANGE_END)
    answer = 'yes' if is_prime(number) else 'no'
    return str(number), answer
