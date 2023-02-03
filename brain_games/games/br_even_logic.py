import random
import brain_games.brain_engine


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def game_logic():
    number = random.randint(1, 100)

    answer = brain_games.brain_engine.ask_question(number)
    correct = 'yes' if is_even(number) else 'no'

    return brain_games.brain_engine.say_result(answer, correct)
