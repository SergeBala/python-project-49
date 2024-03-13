import random
from brain_games.constants import RANGE_START, RANGE_END


def is_even(number):
    return number % 2 == 0


def get_quest_and_answ_even():
    number = random.randint(RANGE_START, RANGE_END)
    answer = 'yes' if is_even(number) else 'no'
    return (number, answer)
