import prompt


def say_hello():
    print('Welcome to the Brain Games!')


def get_user_name():
    return prompt.string('May I have your name? ')


def say_game_over(name, result):
    if result:
        print(f'Congratulations, {name}')
    else:
        print(f"Let's try again, {name}")


def ask_question(question):
    print(f'Question: {question}')


def get_answer():
    return prompt.string('Your answer: ')


def print_result(answer, correct):
    if str(answer) == str(correct):
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
        return False


def game_process(game_description, game_logic):
    say_hello()
    name = get_user_name()
    print(game_description)

    start = 0

    while start < 3:
        win_status = game_logic()
        if not win_status:
            break
        start += 1

    say_game_over(name, win_status)
