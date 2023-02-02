#!/usr/bin/env python3
import random
import brain_games.brain_engine


def main():
    description = 'Answer "yes" if the number is even, otherwise answer "no"'
    brain_games.brain_engine.game_process(description, game_logic)


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def game_logic():
    number = random.randint(1, 100)
    even = is_even(number)

    brain_games.brain_engine.ask_question(number)
    answer = brain_games.brain_engine.get_answer()

    correct = 'yes' if even else 'no'

    return brain_games.brain_engine.print_result(answer, correct)


if __name__ == '__main__':
    main()
