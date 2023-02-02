import random
import brain_games.brain_engine


def main():
    description = 'What number is missing in the progression?'
    brain_games.brain_engine.game_process(description, game_logic)


def generate_progression():
    step = random.randint(2, 9)
    start_num = random.randint(1, 500)
    progression = []
    index = 0

    while index < 10:
        progression.append(start_num)
        start_num += step

        index += 1

    return progression

def game_logic():

    progression = generate_progression()

    change_index = random.randint(0, 9)

    correct = progression[change_index]
    progression[change_index] = '..'

    question = " ".join(map(str, progression[0:10]))

    brain_games.brain_engine.ask_question(question)
    answer = brain_games.brain_engine.get_answer()

    return brain_games.brain_engine.print_result(answer, correct)


if __name__ == '__main__':
    main()
