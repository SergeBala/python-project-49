#!/usr/bin/env python3


import brain_games.games.gcd_game as gcd
import brain_games.common_game_logic as gl
from brain_games.constants import GCD_RULES


def main():
    gl.play_a_game(GCD_RULES, gcd.get_quest_and_answ_gcd)


if __name__ == '__main__':
    main()
