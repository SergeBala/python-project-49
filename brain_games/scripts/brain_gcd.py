#!/usr/bin/env python3


import brain_games.cli as cli
import brain_games.gcd_game as gcd


def main():
    players_name = cli.welcome_user()
    gcd.gcd_game(players_name)


if __name__ == '__main__':
    main()
