# 1- Start the game 
# 2- Prompt the user to enter their name
# 3- Prompt the player to choose their move
# 4- Generate the PC's move randomly
# 5- Determine the winner based on player and PC moves

import random

print("Welcome to Rock, Paper and Scissors Game by Mohamed Khedr")
player_name = (input("Enter you name: ")).capitalize()
print(f"Welcome {player_name}!")

player_Move = (input("Choose your move (Rock, Paper ,Scissors): ").capitalize())
print(f"{player_name}'s move: {player_Move}")

moves = ['Rock', 'Paper', 'Scissors']
pc_Move = random.choice(moves)
print(f"PC's move: {pc_Move}")

if player_Move == pc_Move:
    print("It's a tie")
elif (player_Move == "Rock" and pc_Move == "Scissors"):
    print(f"{player_name} win!")
elif (player_Move == "Paper" and pc_Move == "Rock"):
    print(f"{player_name} win!")
elif (player_Move == "Scissors" and pc_Move == "Papper"):
    print(f"{player_name} win!")
else:
    print(f"{player_name} loses! / PC wins")