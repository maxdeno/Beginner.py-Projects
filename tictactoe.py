# This program develops a two player tic-tac-toe game.
import random
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
current_player = "X"
winner = None
gameRunning = True

print("Welcome! let\'s play and good luck")
# Take the player's input
def player(board):
 try:
    inp = int(input("Enter a number 1-9:"))
    if 1<=inp<= 9 and  board[inp-1] == "-":
        board[inp-1] = current_player
    else:
        print("spot occupied, sorry!")

 except ValueError:
        print("Enter a valid number between 1 and 9! ")

# printing the game board
def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("----")
    print(board[6] + "|" + board[7] + "|" + board[8])


# check for a win or tie
def check_horizontal(board):
    global winner
    if board[0] == board[1] == board [2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def check_row(board):
    global winner
    if board[0] == board[3] == board[6] and board[3] != "-":
        winner = board[3]
        return True
    elif board[1] == board[4] == board[7] and board[4] != "-":
        winner = board[4]
        return True
    elif board[2] == board[5] == board[8] and board[5] != "-":
        winner = board[5]
        return True

def check_diag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def check_tie(board):
    global gameRunning
    if "-" not in board:
        print_board(board)
        print("it\'s a tie!")
        gameRunning = False

def check_winner():
    global gameRunning
    if check_horizontal(board) or check_row(board) or check_diag(board):
        print(f"The winner is {winner}")
        gameRunning = False
# switch the player
def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

# computer
def computer(board):
    while current_player == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switch_player()
# check for the win or tie
while gameRunning:
    print_board(board)
    player(board)
    check_winner()
    if not gameRunning:  # If the game has ended, show the final board
        print_board(board)
        break
    check_tie(board)
    if not gameRunning:  # If it's a tie, show the final board
        print_board(board)
        break
    switch_player()
    computer(board)
    check_winner()
    if not gameRunning:  # If the game has ended, show the final board
        print_board(board)
        break
    check_tie(board)
    if not gameRunning:  # If it's a tie, show the final board
        print_board(board)
        break