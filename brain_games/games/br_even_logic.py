import random


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def game_logic():
    question = random.randint(1, 100)
    correct = 'yes' if is_even(question) else 'no'

    return question, correct
