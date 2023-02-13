import prompt


def run_game(rules, get_round_data):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(rules)

    current_round = 0
    NUMBER_OF_ROUND = 3

    while current_round < NUMBER_OF_ROUND:
        question, correct_answer = get_round_data()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if str(answer) == str(correct_answer):
            print('Correct!')
            win_status = True
        else:
            str_a = f"'{answer}' is wrong answer ;(."
            str_b = f"Correct answer was '{correct_answer}'."
            print(f'{str_a} {str_b}')
            win_status = False

        if not win_status:
            break
        current_round += 1

    if win_status:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
