import random
from brain_games.constants import RANGE_START, RANGE_END


def get_quest_and_answ_calc():
    x = random.randint(RANGE_START, RANGE_END)
    y = random.randint(RANGE_START, RANGE_END)
    operators = ("+", "-", "*")
    operator = random.choice(operators)
    if operator == "+":
        answer = x + y
    elif operator == "-":
        answer = x - y
    elif operator == "*":
        answer = x * y
    return str(x) + " " + operator + " " + str(y), answer
