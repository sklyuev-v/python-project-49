#!/usr/bin/env python3
from brain_games.brain_engine import run_game
from brain_games.games import br_gcd_logic


def main():
    run_game(br_gcd_logic.RULES, br_gcd_logic.get_game_round_data)


if __name__ == '__main__':
    main()
