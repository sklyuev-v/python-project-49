#!/usr/bin/env python3
import random
import brain_games.brain_engine


def main():
    descr = 'Find the greatest common divisor of given numbers.'
    brain_games.brain_engine.game_process(descr, game_logic)


def get_min(num_one, num_two):
    return num_two if num_one > num_two else num_one


def get_gcd(num_one, num_two):
    gcd = get_min(num_one, num_two)

    while True:
        if num_two % gcd == 0 and num_one % gcd == 0:
            break
        else:
            gcd -= 1

    return gcd


def game_logic():
    num_one = random.randint(1, 100)
    num_two = random.randint(1, 100)

    brain_games.brain_engine.ask_question(f'{num_one} {num_two}')
    answer = brain_games.brain_engine.get_answer()
    correct = get_gcd(num_one, num_two)

    return brain_games.brain_engine.say_result(answer, correct)


if __name__ == '__main__':
    main()
