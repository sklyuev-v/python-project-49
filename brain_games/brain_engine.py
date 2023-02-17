import prompt


NUMBER_OF_ROUNDS = 3


def run_game(rules, get_round_data):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}\n{rules}')

    current_round = 0

    while current_round < NUMBER_OF_ROUNDS:
        question, correct_answer = get_round_data()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if str(answer) == str(correct_answer):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return

        current_round += 1

    print(f'Congratulations, {name}!')
