#!/usr/bin/env python3
import random
import brain_games.brain_engine


def main():
    descr = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    brain_games.brain_engine.game_process(descr, game_logic)


def is_prime(number):
    start = 2
    prime = True
    while start < number:
        if number % start == 0:
            prime = False
            break
        start += 1

    return prime


def game_logic():
    number = random.randint(1, 500)

    brain_games.brain_engine.ask_question(number)
    answer = brain_games.brain_engine.get_answer()
    correct = 'yes' if is_prime(number) else 'no'

    return brain_games.brain_engine.say_result(answer, correct)


if __name__ == '__main__':
    main()
