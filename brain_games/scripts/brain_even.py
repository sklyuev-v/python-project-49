import prompt
import random


def main():
        say_welcome()
        get_user_name()
        game_logic()

def say_welcome():
    print('Welcome to the Brain Games!')


def get_user_name():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no"')

    return name


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def game_logic():
    number = random.randint(1, 100)
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    if (answer == 'yes' and is_even(number)) or (answer == 'no' and not is_even(number)):
        print('Correct!')
    else:
        print('Uncorrect')




if __name__ == '__main__':
    main()
