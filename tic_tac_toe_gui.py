import tkinter as tk
import random
from tkinter import messagebox
root = tk.Tk()
root.title("Tic Tac Toe AI")
board = [""] * 9
buttons = []
def check_winner(player):
    win_combinations = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False
def computer_move():
    empty = [i for i in range(9) if board[i] == ""]
     if empty:
        move = random.choice(empty)
        board[move] = "O"
        buttons[move].config(text="O", state="disabled")
        if check_winner("O"):
            messagebox.showinfo("Game Over", "Computer Wins!")
            reset_game()
        elif "" not in board:
            messagebox.showinfo("Game Over", "It's a Draw!")
            reset_game()
def player_move(index):
    if board[index] == "":
        board[index] = "X"
        buttons[index].config(text="X", state="disabled")
        if check_winner("X"):
            messagebox.showinfo("Game Over", "You Win!")
            reset_game()
        elif "" not in board:
            messagebox.showinfo("Game Over", "It's a Draw!")
            reset_game()
        else:
            root.after(500, computer_move)
def reset_game():
    global board
    board = [""] * 9
    for button in buttons:
        button.config(text="", state="normal")
for i in range(9):
    button = tk.Button(
        root,
        text="",
        font=("Arial", 20),
        width=5,
        height=2,
        command=lambda i=i: player_move(i)
    )
    button.grid(row=i//3, column=i%3)
    buttons.append(button)
reset_btn = tk.Button(
    root,
    text="Restart Game",
    font=("Arial", 12),
    command=reset_game
)
reset_btn.grid(row=3, column=0, columnspan=3, sticky="we")
root.mainloop()
