import tkinter as tk
import random

class TicTacToeGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe Almdrasa")
        
        self.player_score, self.computer_score = 0, 0
        self.current_player = 'X'
        self.game = [['' for _ in range(3)] for _ in range(3)]
        self.game_over = False

        self.create_widgets()

    def create_widgets(self):
        self.score_label = tk.Label(self, text=f"You: {self.player_score}   Computer: {self.computer_score}")
        self.score_label.pack()
        
        self.win_lose_tie_label = tk.Label(self, text="", font=("Arial", 12))
        self.win_lose_tie_label.pack()

        self.restart_button = tk.Button(self, text="Restart", command=self.reset_game)
        self.restart_button.pack()

        self.frame = tk.Frame(self)
        self.frame.pack()

        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.frame, text="", width=7, height=3, font=("Arial", 16), command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j)
                self.buttons.append(button)


    def make_move(self, row, col):
        if not self.game_over and self.game[row][col] == '':
            self.game[row][col] = self.current_player
            self.buttons[row * 3 + col].configure(text=self.current_player)
            self.check_winner()
            self.current_player = "X" if self.current_player == "O" else "O"
            self.computer_move()

    def check_winner(self):
        winning_combinations = (
            self.game[0], self.game[1], self.game[2],
            [self.game[i][0] for i in range(3)],
            [self.game[i][1] for i in range(3)],
            [self.game[i][2] for i in range(3)],
            [self.game[i][i] for i in range(3)],
            [self.game[i][2 - i] for i in range(3)]
        )
        for combination in winning_combinations:
            if combination[0] == combination[1] == combination[2] != '':
                self.announce_winner(combination[0])
        
        if all(self.game[i][j] != '' for i in range(3) for j in range(3)):
            self.announce_winner("Draw")

    def announce_winner(self, player):
        self.game_over = True
        if player == "X":
            self.player_score += 1
        elif player == "O":
            self.computer_score += 1
        
        if player != "Draw":
            self.win_lose_tie_label.config(text=f"{player} wins!")
        else:
            self.win_lose_tie_label.config(text="Tie, no winner!")
        
        self.score_label.config(text=f"You: {self.player_score}   Computer: {self.computer_score}")

    def computer_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.game[i][j] == ""]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.game[row][col] = self.current_player
            self.buttons[row * 3 + col].configure(text=self.current_player)
            self.check_winner()
            self.current_player = "X" if self.current_player == "O" else "O"

    def reset_game(self):
        self.game = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.win_lose_tie_label.config(text="")
        self.score_label.config(text=f"You: {self.player_score}   Computer: {self.computer_score}")
        self.game_over = False
        for button in self.buttons:
            button.config(text="")

if __name__ == "__main__":
    game = TicTacToeGame()
    game.mainloop()
