#!/usr/bin/env python3


import brain_games.cli as cli
import brain_games.games.even_game as evg


def main():
    players_name = cli.welcome_user()
    evg.even_game(players_name)


if __name__ == '__main__':
    main()
