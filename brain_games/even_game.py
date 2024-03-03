import random
import brain_games.common_game_logic as gl


def is_even(number):
    return number % 2 == 0


def get_random_number(start_of_range=0, end_of_range=1000):
    return random.randint(start_of_range, end_of_range)


def get_corr_answ_even_g(number):
    if is_even(number):
        answer = 'yes'
    else:
        answer = 'no'
    return answer


def even_game_new(players_name):
    rules = "Answer \"yes\" if the number is even, otherwise answer \"no\"."
    gl.play_a_game(players_name, rules, get_random_number, get_corr_answ_even_g)
