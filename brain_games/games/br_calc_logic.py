import random


MIN_NUMBER = 1
MAX_NUMBER = 100
RULES = 'What is the result of the expression?'


def get_game_round_data():
    num_one = random.randint(MIN_NUMBER, MAX_NUMBER)
    num_two = random.randint(MIN_NUMBER, MAX_NUMBER)
    sign = random.choice(('+', '-', '*'))

    match sign:
        case '+':
            correct_answer = num_one + num_two
        case '-':
            correct_answer = num_one - num_two
        case '*':
            correct_answer = num_one * num_two

    question = f'{num_one} {sign} {num_two}'

    return question, correct_answer
