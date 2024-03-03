import brain_games.common_game_logic as gl
import random
from brain_games.even_game import get_random_number


def get_quest_and_answ_calc():
    x = get_random_number()
    y = get_random_number()
    operators = ("+", "-", "*")
    operator = random.choice(operators)
    if operator == "+":
        answer = x + y
    elif operator == "-":
        answer = x - y
    elif operator == "*":
        answer = x * y
    return str(x) + " " + operator + " " + str(y), answer


def calc_game(players_name):
    rules = "What is the result of the expression?"
    gl.play_a_game(players_name, rules, get_quest_and_answ_calc)
