#!/usr/bin/env python3


import brain_games.cli as cli
import brain_games.games.prime_game as prm


def main():
    players_name = cli.welcome_user()
    prm.prime_game(players_name)


if __name__ == '__main__':
    main()
