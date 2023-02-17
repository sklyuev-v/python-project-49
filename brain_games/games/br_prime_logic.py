import random


MIN_NUMBER = 1
MAX_NUMBER = 500
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    start = 2
    prime = True
    while start < number:
        if number % start == 0:
            prime = False
            break
        start += 1

    return prime


def get_game_round_data():
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_prime(question) else 'no'

    return question, correct_answer
