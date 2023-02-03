#!/usr/bin/env python3
from brain_games.brain_engine import run_game
from brain_games.games.br_prime_logic import game_logic


def main():
    descr = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    run_game(descr, game_logic)


if __name__ == '__main__':
    main()
