#!/usr/bin/env python3


import brain_games.games.even_game as evg
import brain_games.common_game_logic as gl
from brain_games.constants import EVEN_RULES


def main():
    gl.play_a_game(EVEN_RULES, evg.get_quest_and_answ_even)


if __name__ == '__main__':
    main()
