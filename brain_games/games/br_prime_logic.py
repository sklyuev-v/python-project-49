import random
import brain_games.brain_engine


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

    answer = brain_games.brain_engine.ask_question(number)
    correct = 'yes' if is_prime(number) else 'no'

    return brain_games.brain_engine.say_result(answer, correct)
