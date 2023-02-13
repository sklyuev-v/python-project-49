#!/usr/bin/env python3
from brain_games.brain_engine import run_game
from brain_games.games import br_progression_logic


def main():
    run_game(br_progression_logic.RULES, br_progression_logic.get_round_data)


if __name__ == '__main__':
    main()
