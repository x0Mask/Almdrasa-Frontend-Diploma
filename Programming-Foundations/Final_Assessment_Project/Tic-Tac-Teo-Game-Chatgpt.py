import tkinter as tk
import random

class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.player = "X"
        self.computer = "O"
        self.score_player = 0
        self.score_computer = 0
        self.winner_text = tk.StringVar()
        self.winner_text.set("")
        self.game_over = False

        self.create_widgets()

    def create_widgets(self):
        self.score_label = tk.Label(self.root, text="You: 0  Computer: 0", font=("Arial", 12))
        self.score_label.grid(row=0, column=0, columnspan=3)

        self.winner_display = tk.Label(self.root, textvariable=self.winner_text, font=("Arial", 12))
        self.winner_display.grid(row=1, column=0, columnspan=3)

        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_game)
        self.restart_button.grid(row=2, column=0, columnspan=3)

        self.buttons = [[tk.Button(self.root, text="", font=("Arial", 20), width=5, height=2,
                                   command=lambda row=i, col=j: self.player_move(row, col)) for j in range(3)] for i in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i + 3, column=j)
                self.buttons[i][j].config(bg="#D0D0CF")

    def check_winner(self, board):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != "":
                return board[i][0]
            if board[0][i] == board[1][i] == board[2][i] != "":
                return board[0][i]
        if board[0][0] == board[1][1] == board[2][2] != "":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != "":
            return board[0][2]
        return None

    def computer_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.buttons[i][j]["text"] == ""]
        if empty_cells and not self.game_over:
            i, j = random.choice(empty_cells)
            self.buttons[i][j]["text"] = self.computer
            self.buttons[i][j].config(state="disabled", disabledforeground="black")
            self.check_game_status()

    def player_move(self, row, col):
        if self.buttons[row][col]["text"] == "" and not self.game_over:
            self.buttons[row][col]["text"] = self.player
            self.buttons[row][col].config(state="disabled", disabledforeground="black")
            self.buttons[row][col].config(bg="light blue")
            self.check_game_status()
            self.computer_move()

    def check_game_status(self):
        winner = self.check_winner([[self.buttons[i][j]["text"] for j in range(3)] for i in range(3)])
        if winner:
            self.winner_text.set(f"{winner} wins!")
            if winner == self.player:
                self.score_player += 1
            else:
                self.score_computer += 1
            self.update_score()
            self.disable_buttons()
            self.game_over = True
        elif all(self.buttons[i][j]["text"] for i in range(3) for j in range(3)):
            self.winner_text.set("Tie, no winner!")
            self.update_score()
            self.disable_buttons()
            self.game_over = True
            for i in range(3):
                for j in range(3):
                    self.buttons[i][j].config(bg="red")
            self.save_stats()

    def update_score(self):
        self.score_label.config(text=f"You: {self.score_player}  Computer: {self.score_computer}")
        self.save_stats()

    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")

    def restart_game(self):
        self.game_over = False
        self.winner_text.set("")
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", state="normal", bg="#D0D0CF")
    
    def load_stats(self):
        file_list = glob.glob('game_stats.txt')
        if file_list:
            with open(file_list[0], 'r') as file:
                stats = file.read().split(',')
                self.score_player = int(stats[0])
                self.score_computer = int(stats[1])
        else:
            self.score_player, self.score_computer = 0, 0

        self.update_score()

    def save_stats(self):
        with open('game_stats.txt', 'w') as file:
            file.write(f"{self.score_player},{self.score_computer}")


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()
