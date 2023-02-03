import prompt
 

def get_user_name():
    print('Welcome to the Brain Games!')
    return prompt.string('May I have your name? ')


def ask_question(question):
    print(f'Question: {question}')
    return prompt.string('Your answer: ')


def say_result(answer, correct):
    if str(answer) == str(correct):
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
        return False


def say_game_over(name, result):
    if result:
        print(f'Congratulations, {name}')
    else:
        print(f"Let's try again, {name}")


def run_game(game_description, game_logic):
    name = get_user_name()
    print(game_description)

    number_of_round = 0

    while number_of_round < 3:
        win_status = game_logic()
        if not win_status:
            break
        number_of_round += 1

    say_game_over(name, win_status)
