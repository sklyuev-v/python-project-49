#!/usr/bin/env python3
from brain_games.brain_engine import run_game
from brain_games.games.br_gcd_logic import game_logic


def main():
    description = 'Find the greatest common divisor of given numbers.'
    run_game(description, game_logic)


if __name__ == '__main__':
    main()
