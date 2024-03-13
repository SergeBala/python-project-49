#!/usr/bin/env python3


import brain_games.games.prime_game as prime
import brain_games.common_game_logic as gl
from brain_games.constants import PRIM_RULES


def main():
    gl.play_a_game(PRIM_RULES, prime.get_quest_and_answ_prime)


if __name__ == '__main__':
    main()
