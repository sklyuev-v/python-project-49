import random


MIN_NUMBER = 1
MAX_NUMBER = 100
RULES = 'Find the greatest common divisor of given numbers.'


def get_gcd(num_one, num_two):
    if num_one == 0:
        return num_two

    return get_gcd(num_two % num_one, num_one)


def get_game_round_data():
    num_one = random.randint(MIN_NUMBER, MAX_NUMBER)
    num_two = random.randint(MIN_NUMBER, MAX_NUMBER)

    question = (f'{num_one} {num_two}')
    correct_answer = get_gcd(num_one, num_two)

    return question, correct_answer
