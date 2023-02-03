#!/usr/bin/env python3
from brain_games.brain_engine import run_game
from brain_games.games.br_calc_logic import game_logic


def main():
    run_game('What is the result of the expression?', game_logic)


if __name__ == '__main__':
    main()
