"""This is a guessing game script"""

import random

attempts_list = []


def display_score():
    if not attempts_list:
        print("No scores to display, Start Guessing!")
    else:
        print(f" {player_name}'s highest score is {min(attempts_list)} attempts ")


ATTEMPTS = 0
rand_number = random.randint(0, 10)

print("Hello player!, Welcome to the guessing game")
player_name = input("What is your name? ")
wanna_play = input(
    f"Would like to play the guessing game?"
    " Enter(yes/no) "
).lower()

if wanna_play == "no":
    print("That's nice, I like your challenge spirit")
    exit()
else:
    display_score()

while wanna_play == "yes":
    try:
        guess = int(input(f"Please choose a number between 1 and 10: "))
        if (guess < 0 or guess > 10):
            raise ValueError("Please choose a number within the given range.")
        
        ATTEMPTS += 1

        if guess == rand_number:
            print("Good guess, You get it")
            print(f"It took you {ATTEMPTS} attempts")
            wanna_play = input("Would like to increase your score? (Enter Yes/No): ").lower()

            attempts_list.append(ATTEMPTS)

            if wanna_play == "No":
                print("Thanks for Trying, Have a good day!")
            else:
                ATTEMPTS = 0
                rand_number = random.randint(1, 10)
                display_score()
                continue
        elif guess < rand_number:
            print("It's higher")
        else:
            print("It's lower")
    except ValueError as err:
        print(err)
