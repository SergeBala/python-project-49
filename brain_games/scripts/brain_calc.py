#!/usr/bin/env python3


import brain_games.games.calc_game as calc
import brain_games.common_game_logic as gl
from brain_games.constants import CALC_RULES


def main():
    gl.play_a_game(CALC_RULES, calc.get_quest_and_answ_calc)


if __name__ == '__main__':
    main()
