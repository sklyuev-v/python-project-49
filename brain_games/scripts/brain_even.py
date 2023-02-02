#!/usr/bin/env python3
import prompt
import random
import brain_games.brain_engine


def main():
    brain_games.brain_engine.say_hello()
    name = brain_games.brain_engine.get_user_name()
    game_logic(name)


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def game_logic(user_name):
    print('Answer "yes" if the number is even, otherwise answer "no"')

    win = True
    index = 0

    while index < 3:
        number = random.randint(1, 100)
        even = is_even(number)
        corr = 'yes' if even else 'no'
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if (answer == 'yes' and even) or (answer == 'no' and not even):
            print('Correct!')
        else:
            print(f"{answer}' is wrong answer ;(. Correct answer was '{corr}'.")
            win = False
            break
        index += 1

    brain_games.brain_engine.say_game_over(user_name, win)


if __name__ == '__main__':
    main()
