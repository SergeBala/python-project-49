#!/usr/bin/env python3


import brain_games.games.progression_game as prog
import brain_games.common_game_logic as gl
from brain_games.constants import PROG_RULES


def main():
    gl.play_a_game(PROG_RULES, prog.get_quest_and_answ_prog)


if __name__ == '__main__':
    main()
