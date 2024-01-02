import random

class GuessingGame:
    def __init__(self):
        self.player_name = ""
        self.attempts_list = []

    def display_score(self):
        """
        Display the player's highest score.
        """
        if self.attempts_list:
            print(f"{self.player_name}'s highest score is {min(self.attempts_list)} attempts")
        else:
            print("No scores to display. Start guessing!")

    def play_game(self):
        """
        Execute the guessing game logic.
        Returns the number of attempts taken.
        """
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

                    self.attempts_list.append(attempts)
                    return attempts

                elif guess < rand_number:
                    print("It's higher.")
                else:
                    print("It's lower.")

            except ValueError as err:
                print(err)

    def start_game(self):
        """
        Start the guessing game.
        """
        print("Hello player! Welcome to the guessing game")
        self.player_name = input("What is your name? ")

        while True:
            wanna_play = input("Would you like to play the guessing game? (yes/no): ").lower()

            if wanna_play == "no":
                print("Thanks.")
                break

            elif wanna_play == "yes":
                self.display_score()

                if self.attempts_list and input("Would you like to view your high score? (yes/no): ").lower() == "yes":
                    self.display_score()

                self.attempts_list.append(self.play_game())

            else:
                print("Invalid input. Please enter 'yes' or 'no'.")



