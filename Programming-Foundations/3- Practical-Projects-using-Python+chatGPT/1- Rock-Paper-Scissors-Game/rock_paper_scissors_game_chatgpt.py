import random

def get_player_name() -> str:
    """Prompt the user to enter their name."""
    return input("Enter your name: ")

def get_player_choice() -> str:
    """Prompt the player to choose their move."""
    while True:
        player_choice = input("Choose your move (Rock, Paper, Scissors): ").capitalize()
        if player_choice in ['Rock', 'Paper', 'Scissors']:
            return player_choice
        else:
            print("Invalid move! Please choose from Rock, Paper, or Scissors.")

def get_pc_choice() -> str:
    """Generate the PC's move randomly."""
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)

def determine_winner(player_choice: str, pc_choice: str, player_name: str) -> str:
    """Determine the winner based on player and PC choices."""
    winning_combinations = {
        ('Rock', 'Scissors'): f"{player_name} wins!",
        ('Paper', 'Rock'): f"{player_name} wins!",
        ('Scissors', 'Paper'): f"{player_name} wins!",
        ('Rock', 'Paper'): f"{player_name} loses! / PC wins",
        ('Paper', 'Scissors'): f"{player_name} loses! / PC wins",
        ('Scissors', 'Rock'): f"{player_name} loses! / PC wins",
    }
    if player_choice == pc_choice:
        return "It's a tie!"
    return winning_combinations.get((player_choice, pc_choice), '')

def play_game() -> None:
    """Start the Rock, Paper, Scissors game."""
    print("Welcome to Rock, Paper, and Scissors Game by Mohamed Khedr")

    player_name = get_player_name()
    print(f"Welcome, {player_name}!")

    player_choice = get_player_choice()
    print(f"{player_name}'s move: {player_choice}")

    pc_choice = get_pc_choice()
    print(f"PC's move: {pc_choice}")

    result = determine_winner(player_choice, pc_choice, player_name)
    print(result)

# Run the game
play_game()