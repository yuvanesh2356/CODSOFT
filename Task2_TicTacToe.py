import tkinter as tk
from tkinter import messagebox
import math
import random

#WINDOW
root = tk.Tk()
root.title("Tic Tac Toe AI")
root.geometry("500x650")
root.config(bg="#0F172A")

#VARIABLES
board = [" " for _ in range(9)]
buttons = []
human = "X"
ai = "O"
game_over = False

#TITLE
title = tk.Label(
    root,
    text="TIC TAC TOE",
    font=("Arial", 28, "bold"),
    bg="#0F172A",
    fg="#FFFFFF"
)
title.pack(pady=20)

status_label = tk.Label(
    root,
    text="Your Turn",
    font=("Arial", 16,"bold"),
    bg="#0F172A",
    fg="#FFFFFF"
)
status_label.pack(pady=10)

#GAME FRAME
frame = tk.Frame(root, bg="#0F172A")
frame.pack()

#WIN CHECK
def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return pos

    return None

#DRAW CHECK
def is_draw():
    return " " not in board

#MINIMAX WITH ALPHA-BETA
def minimax(depth, is_maximizing, alpha, beta):

    if check_winner(ai):
        return 10 - depth

    if check_winner(human):
        return depth - 10

    if is_draw():
        return 0

    # AI Turn
    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = ai

                score = minimax(depth + 1, False, alpha, beta)

                board[i] = " "

                best_score = max(best_score, score)
                alpha = max(alpha, score)

                # Alpha-Beta Pruning
                if beta <= alpha:
                    break

        return best_score

    # Human Turn
    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = human

                score = minimax(depth + 1, True, alpha, beta)

                board[i] = " "

                best_score = min(best_score, score)
                beta = min(beta, score)

                # Alpha-Beta Pruning
                if beta <= alpha:
                    break

        return best_score

#AI MOVE
def ai_move():

    best_score = -math.inf
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = ai

            score = minimax(0, False, -math.inf, math.inf)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    if move is not None:
        board[move] = ai
        buttons[move].config(text=ai, fg="#FBBF24")

    check_game()

    if not game_over:
        status_label.config(text="Your Turn")

#PLAYER MOVE
def player_move(index):

    global game_over

    if board[index] == " " and not game_over:

        board[index] = human
        buttons[index].config(text=human, fg="#F8FAFC")

        check_game()

        if not game_over:
            status_label.config(text="Computer Turn")
            root.after(500, ai_move)

#CHECK GAME
def check_game():

    global game_over

    # Human Win
    win = check_winner(human)

    if win:
        game_over = True

        for i in win:
            buttons[i].config(bg="#22C55E")

        status_label.config(text="You Win!")
        messagebox.showinfo("Game Over", "You Won!")
        return

    # AI Win
    win = check_winner(ai)

    if win:
        game_over = True

        for i in win:
            buttons[i].config(bg="#22C55E")

        status_label.config(text="AI Wins!")
        messagebox.showinfo("Game Over", "AI Won!")
        return

    # Draw
    if is_draw():
        game_over = True
        status_label.config(text="Match Draw!")
        messagebox.showinfo("Game Over", "It's a Draw!")

#RESET GAME
def reset_game():

    global board, game_over

    board = [" " for _ in range(9)]
    game_over = False

    for button in buttons:
        button.config(
            text="",
            bg="#2d2d2d"
        )

    status_label.config(text="Your Turn")

#BUTTONS
for i in range(9):

    button = tk.Button(
        frame,
        text="",
        font=("Arial", 28, "bold"),
        width=5,
        height=2,
        bg="#1E293B",
        fg="white",
        activebackground="#444",
        command=lambda i=i: player_move(i)
    )

    button.grid(row=i//3, column=i%3, padx=5, pady=5)

    buttons.append(button)

#RESET BUTTON
reset_btn = tk.Button(
    root,
    text="Restart Game",
    font=("Arial", 16, "bold"),
    bg="lightgrey",
    fg="black",
    padx=10,
    pady=5,
    command=reset_game
)

reset_btn.pack(pady=25)



#RUN
root.mainloop()
