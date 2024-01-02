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
        