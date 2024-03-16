#!/usr/bin/env python3


from brain_games.games.even_game import get_quest_and_answ_even, EVEN_RULES
from brain_games.common_game_logic import play_a_game


def main():
    play_a_game(EVEN_RULES, get_quest_and_answ_even)


if __name__ == '__main__':
    main()
