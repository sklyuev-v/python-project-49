import random


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
    question = random.randint(1, 500)
    correct = 'yes' if is_prime(question) else 'no'

    return question, correct
