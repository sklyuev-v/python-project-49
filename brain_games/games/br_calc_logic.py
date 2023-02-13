import random


RULES = 'What is the result of the expression?'


def game_logic():
    MIN_NUMBER = 1
    MAX_NUMBER = 100

    num_one = random.randint(MIN_NUMBER, MAX_NUMBER)
    num_two = random.randint(MIN_NUMBER, MAX_NUMBER)
    sign = random.choice(('+', '-', '*'))

    if sign == '+':
        correct = num_one + num_two
    elif sign == '-':
        correct = num_one - num_two
    else:
        correct = num_one * num_two

    question = f'{num_one} {sign} {num_two}'

    return question, correct
