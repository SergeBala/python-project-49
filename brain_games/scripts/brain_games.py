#!/usr/bin/env python3
from brain_games.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")
    players_name = welcome_user()
    return players_name


if __name__ == '__main__':
    main()
