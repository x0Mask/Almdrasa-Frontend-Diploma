"""This is a guessing game script"""

import random

attempts_list = []

def display_score():
    if not attempts_list:
        print("No scores to display, Start Guessing!")    
    else:
        print(f"The {player_name} high score is {min(attempts_list)} attempts ")

attempts = 0
rand_number = random.randint(0, 10)

print("Hello player!, Welcome to the guessing game")
player_name = input("What is your name? ")
wanna_play = input(
    f"Would like to play the guessing game?"
    " Enter(yes/no) "
).lower()

if wanna_play == "yes":
    print("That's nice, I like your challenge spirit")
    exit()
else:
    display_score()

while wanna_play == "yes":
    guess = int(input(f"Please choose a number between 1 and 10: "))
    if (guess < 0 or guess > 10):
        raise(ValueError("Please choose a number within the given range."))

