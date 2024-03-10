import brain_games.common_game_logic as gl
from brain_games.even_game import get_random_number


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
    number = get_random_number()
    answer = is_prime(number)
    return str(number), answer


def prime_game(players_name):
    rules = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."
    gl.play_a_game(players_name, rules, get_quest_and_answ_prime)
