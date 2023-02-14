import random


RULES = 'Find the greatest common divisor of given numbers.'


def get_gcd(num_one, num_two):
    gcd = min(num_one, num_two)

    while True:
        if num_two % gcd == 0 and num_one % gcd == 0:
            break
        else:
            gcd -= 1

    return gcd


def get_game_round_data():
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    num_one = random.randint(MIN_NUMBER, MAX_NUMBER)
    num_two = random.randint(MIN_NUMBER, MAX_NUMBER)

    question = (f'{num_one} {num_two}')
    correct_answer = get_gcd(num_one, num_two)

    return question, correct_answer
