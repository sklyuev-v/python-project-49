#!/usr/bin/env python3
from brain_games.brain_engine import run_game
from brain_games.games.br_even_logic import game_logic


def main():
    description = 'Answer "yes" if the number is even, otherwise answer "no"'
    run_game(description, game_logic)


if __name__ == '__main__':
    main()
