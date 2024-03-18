from random import randint, choice
from brain_games.constants import RANGE_START, RANGE_END


RULES = "What is the result of the expression?"


def get_quest_and_answ():
    x = randint(RANGE_START, RANGE_END)
    y = randint(RANGE_START, RANGE_END)
    operators = ("+", "-", "*")
    operator = choice(operators)
    if operator == "+":
        answer = x + y
    elif operator == "-":
        answer = x - y
    elif operator == "*":
        answer = x * y
    return f"{x} {operator} {y}", answer
