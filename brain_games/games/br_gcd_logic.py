import random
import brain_games.brain_engine


def get_gcd(num_one, num_two):
    gcd = min(num_one, num_two)

    while True:
        if num_two % gcd == 0 and num_one % gcd == 0:
            break
        else:
            gcd -= 1

    return gcd


def game_logic():
    num_one = random.randint(1, 100)
    num_two = random.randint(1, 100)

    answer = brain_games.brain_engine.ask_question(f'{num_one} {num_two}')
    correct = get_gcd(num_one, num_two)

    return brain_games.brain_engine.say_result(answer, correct)
