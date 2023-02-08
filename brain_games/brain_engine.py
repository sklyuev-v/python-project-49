import prompt


def run_game(game_description, game_logic):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game_description)

    number_of_round = 0

    while number_of_round < 3:
        question, corr = game_logic()
        print(f'Question: {question}')
        ans = prompt.string('Your answer: ')

        if str(ans) == str(corr):
            print('Correct!')
            win_status = True
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{corr}'.")
            win_status = False

        if not win_status:
            break
        number_of_round += 1

    if win_status:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
