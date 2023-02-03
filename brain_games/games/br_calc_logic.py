import random
import brain_games.brain_engine


def game_logic():
    num_one = random.randint(1, 100)
    num_two = random.randint(1, 100)
    sign = random.choice(('+', '-', '*'))

    if sign == '+':
        correct = num_one + num_two
    elif sign == '-':
        correct = num_one - num_two
    else:
        correct = num_one * num_two

    question = f'{num_one} {sign} {num_two}'
    answer = brain_games.brain_engine.ask_question(question)

    return brain_games.brain_engine.say_result(answer, correct)
