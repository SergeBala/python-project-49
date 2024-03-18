from random import randint
from brain_games.constants import RANGE_START, RANGE_END


RULES = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def is_even(number):
    return number % 2 == 0


def get_quest_and_answ():
    number = randint(RANGE_START, RANGE_END)
    answer = 'yes' if is_even(number) else 'no'
    return (number, answer)
