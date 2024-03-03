#!/usr/bin/env python3


import brain_games.cli as cli
import brain_games.calc_game as calc


def main():
    players_name = cli.welcome_user()
    calc.calc_game(players_name)


if __name__ == '__main__':
    main()
