#!/usr/bin/env python3
import brain_games.cli


def say_hello():
    print('Welcome to the Brain Games!')


def main():
    say_hello()
    brain_games.cli.welcome_user()


if __name__ == '__main__':
    main()
