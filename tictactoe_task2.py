import tkinter as tk
import math

# Define the Tic-Tac-Toe board
board = [[' ' for _ in range(3)] for _ in range(3)]
human = 'X'
ai = 'O'
current_turn = human

def check_winner(board, player):
    for row in range(3):
        if all([cell == player for cell in board[row]]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    return all([cell != ' ' for row in board for cell in row])

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, ai):
        return 1
    if check_winner(board, human):
        return -1
    if check_draw(board):
        return 0
    
    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = ai
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = human
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def best_move(board):
    best_val = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = ai
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = ' '
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    return move

def on_click(row, col):
    global current_turn
    if board[row][col] == ' ' and current_turn == human:
        board[row][col] = human
        buttons[row][col].config(text=human)
        if check_winner(board, human):
            status_label.config(text="Human wins!")
            disable_all_buttons()
            play_again_button.pack()
            return
        elif check_draw(board):
            status_label.config(text="It's a draw!")
            disable_all_buttons()
            play_again_button.pack()
            return
        current_turn = ai
        ai_move()

def ai_move():
    global current_turn
    row, col = best_move(board)
    board[row][col] = ai
    buttons[row][col].config(text=ai)
    if check_winner(board, ai):
        status_label.config(text="AI wins!")
        disable_all_buttons()
        play_again_button.pack()
        return
    elif check_draw(board):
        status_label.config(text="It's a draw!")
        disable_all_buttons()
        play_again_button.pack()
        return
    current_turn = human

def disable_all_buttons():
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(state=tk.DISABLED)

def reset_game():
    global board, current_turn
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_turn = human
    status_label.config(text="Human's Turn")
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=' ', state=tk.NORMAL)
    play_again_button.pack_forget()

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create status label
status_label = tk.Label(root, text="Human's Turn", font=('Helvetica', 16))
status_label.pack(side="top")

# Create the Tic-Tac-Toe grid
frame = tk.Frame(root)
frame.pack()

buttons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(frame, text=' ', font=('Helvetica', 20), height=3, width=6,
                                      command=lambda r=row, c=col: on_click(r, c))
        buttons[row][col].grid(row=row, column=col)

# Create the Play Again button
play_again_button = tk.Button(root, text="Play Again", font=('Helvetica', 16), command=reset_game)
play_again_button.pack_forget()

# Start the GUI event loop
root.mainloop()
