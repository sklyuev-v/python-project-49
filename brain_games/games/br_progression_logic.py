import random


MIN_NUMBER = 1
MAX_NUMBER = 500
MIN_DIFFERENCE = 2
MAX_DIFFERENCE = 9
LENGTH_PROGRESSION = 10
RULES = 'What number is missing in the progression?'


def create_progression(initial_term, common_difference):
    last_term = initial_term + common_difference * LENGTH_PROGRESSION
    return list(range(initial_term, last_term, common_difference))


def make_question(progression, hide_term_index):
    correct_answer = progression[hide_term_index]
    progression[hide_term_index] = '..'
    return ' '.join(map(str, progression)), correct_answer


def get_round_data():
    initial_term = random.randint(MIN_NUMBER, MAX_NUMBER)
    common_difference = random.randint(MIN_DIFFERENCE, MAX_DIFFERENCE)

    progression = create_progression(initial_term, common_difference)

    hide_term_index = random.randint(0, len(progression) - 1)
    question, corr_ans = make_question(progression, hide_term_index)

    return question, corr_ans
