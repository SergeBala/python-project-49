#!/usr/bin/env python3


from brain_games.games.prime_game import get_quest_and_answ_prime, PRIM_RULES
from brain_games.common_game_logic import play_a_game


def main():
    play_a_game(PRIM_RULES, get_quest_and_answ_prime)


if __name__ == '__main__':
    main()
