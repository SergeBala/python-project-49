#!/usr/bin/env python3


from brain_games.games.calc_game import get_quest_and_answ_calc, CALC_RULES
from brain_games.common_game_logic import play_a_game


def main():
    play_a_game(CALC_RULES, get_quest_and_answ_calc)


if __name__ == '__main__':
    main()
