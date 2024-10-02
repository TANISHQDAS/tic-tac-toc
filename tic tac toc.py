import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")
        self.master.configure(bg="black")
        
        self.current_player = "X"
        self.game_over = False
        self.board = [[None for _ in range(3)] for _ in range(3)]

        self.turn_label = tk.Label(master, text="Player X's Turn", bg="red", fg="white", font=("Arial", 16))
        self.turn_label.grid(row=0, column=0, columnspan=3)

        for row in range(3):
            for col in range(3):
                button = tk.Button(master, text="", width=10, height=3, bg="black", fg="white",
                                   command=lambda r=row, c=col: self.click(r, c))
                button.grid(row=row + 1, column=col)
                self.board[row][col] = button

    def click(self, row, col):
        if self.board[row][col]["text"] == "" and not self.game_over:
            self.board[row][col]["text"] = self.current_player
            self.board[row][col].config(bg="blue" if self.current_player == "X" else "red")
            if self.check_winner():
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.game_over = True
                self.play_again()
            elif self.check_draw():
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                self.game_over = True
                self.play_again()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.update_turn_label()

    def check_winner(self):
        for row in self.board:
            if row[0]["text"] == row[1]["text"] == row[2]["text"] != "":
                return True
        for col in range(3):
            if self.board[0][col]["text"] == self.board[1][col]["text"] == self.board[2][col]["text"] != "":
                return True
        if self.board[0][0]["text"] == self.board[1][1]["text"] == self.board[2][2]["text"] != "":
            return True
        if self.board[0][2]["text"] == self.board[1][1]["text"] == self.board[2][0]["text"] != "":
            return True
        return False

    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell["text"] == "":
                    return False
        return True

    def update_turn_label(self):
        self.turn_label.config(text=f"Player {self.current_player}'s Turn", bg="red" if self.current_player == "X" else "blue")

    def play_again(self):
        answer = messagebox.askyesno("Tic-Tac-Toe", "Do you want to play again?")
        if answer:
            self.reset_board()
        else:
            self.master.quit()

    def reset_board(self):
        self.game_over = False
        self.current_player = "X"
        self.turn_label.config(text="Player X's Turn", bg="red")
        for row in self.board:
            for button in row:
                button["text"] = ""
                button.config(bg="black")

if __name__ == "__main__":
    window = tk.Tk()
    game = TicTacToe(window)
    window.mainloop()
