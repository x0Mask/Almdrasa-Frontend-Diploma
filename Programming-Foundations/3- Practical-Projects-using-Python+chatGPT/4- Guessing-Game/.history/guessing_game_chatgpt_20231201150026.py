import random

attempts_list = []


def display_score():
    if attempts_list:
        print(f"{player_name}'s highest score is {min(attempts_list)} attempts")
    else:
        print("No scores to display. Start guessing!")


def play_game():
    attempts = 0
    rand_number = random.randint(1, 10)

    while True:
        try:
            guess = int(input("Please choose a number between 1 and 10: "))
            if guess not in range(1, 11):
                raise ValueError("Please choose a number within the given range.")

            attempts += 1

            if guess == rand_number:
                print("Good guess! You got it.")
                print(f"It took you {attempts} attempts.")

                attempts_list.append(attempts)
                return attempts

            elif guess < rand_number:
                print("It's higher.")
            else:
                print("It's lower.")

        except ValueError as err:
            print(err)


print("Hello player! Welcome to the guessing game")
player_name = input("What is your name? ")

while True:
    wanna_play = input("Would you like to play the guessing game? (yes/no): ").lower()

    if wanna_play == "no":
        print("That's nice! I like your challenge spirit.")
        break

    elif wanna_play == "yes":
        display_score()

        if attempts_list and input("Would you like to view your high score? (yes/no): ").lower() == "yes":
            display_score()

        attempts_list.append(play_game())

    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
