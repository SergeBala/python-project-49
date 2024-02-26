#!/usr/bin/env python3


import brain_games.scripts.brain_games as bg
import brain_games.even_game as evg


def main():
    players_name = bg.main()
    evg.even_game(players_name, 3)


if __name__ == '__main__':
    main()
