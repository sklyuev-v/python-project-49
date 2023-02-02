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
