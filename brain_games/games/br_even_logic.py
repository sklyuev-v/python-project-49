import random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return True if number % 2 == 0 else False


def get_game_round_data():
    MIN_NUMBER = 1
    MAX_NUMBER = 100

    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_even(question) else 'no'

    return question, correct_answer
