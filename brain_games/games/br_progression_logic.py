import random


RULES = 'What number is missing in the progression?'


def create_progression(initial_term, common_difference):
    LENGTH_PROGRESSION = 10
    last_term = initial_term + common_difference * LENGTH_PROGRESSION
    return list(range(initial_term, last_term, common_difference))


def convert_progression_to_str(progression):
    return ' '.join(map(str, progression))


def get_round_data():
    MIN_NUMBER = 1
    MAX_NUMBER = 500
    initial_term = random.randint(MIN_NUMBER, MAX_NUMBER)

    MIN_DIFFERENCE = 2
    MAX_DIFFERENCE = 9
    common_difference = random.randint(MIN_DIFFERENCE, MAX_DIFFERENCE)

    progression = create_progression(initial_term, common_difference)

    question_index = random.randint(0, len(progression) - 1)

    correct_answer = progression[question_index]
    progression[question_index] = '..'

    question = convert_progression_to_str(progression)

    return question, correct_answer
