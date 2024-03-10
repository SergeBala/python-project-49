#!/usr/bin/env python3


import brain_games.cli as cli
import brain_games.progression_game as prog


def main():
    players_name = cli.welcome_user()
    prog.progression_game(players_name)


if __name__ == '__main__':
    main()
