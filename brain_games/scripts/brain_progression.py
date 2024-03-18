#!/usr/bin/env python3


from brain_games.games.prog_game import get_quest_and_answ_prog, PROG_RULES
from brain_games.common_game_logic import run_game


def main():
    run_game(PROG_RULES, get_quest_and_answ_prog)


if __name__ == '__main__':
    main()
