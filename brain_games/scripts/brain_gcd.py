#!/usr/bin/env python3


from brain_games.games.gcd_game import get_quest_and_answ_gcd, GCD_RULES
from brain_games.common_game_logic import play_a_game


def main():
    play_a_game(GCD_RULES, get_quest_and_answ_gcd)


if __name__ == '__main__':
    main()
