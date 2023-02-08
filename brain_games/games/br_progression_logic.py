import random


def game_logic():

    start = random.randint(1, 500)
    step = random.randint(2, 9)
    stop = start + step * 10

    change_index = random.randint(0, 9)

    progression = range(start, stop, step)
    question = ''

    for (index, number) in enumerate(progression):
        if index == change_index:
            correct = number
            question += '..' + ' '
        else:
            question += str(number) + ' '

    return question, correct
