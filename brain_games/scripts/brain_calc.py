#!/usr/bin/env python3
import random
import brain_games.brain_engine


def main():
    description = 'What is the result of the expression?'
    brain_games.brain_engine.game_process(description, game_process)


def game_process():
    num_one = random.randint(1, 100)
    num_two = random.randint(1, 100)
    sign = random.choice(('+', '-', '*'))

    if sign == '+':
        correct = num_one + num_two
    elif sign == '-':
        correct = num_one - num_two
    else:
        correct = num_one * num_two

    brain_games.brain_engine.ask_question(f'{num_one} {sign} {num_two}')
    answer = brain_games.brain_engine.get_answer()

    return brain_games.brain_engine.print_result(answer, correct)


if __name__ == '__main__':
    main()
