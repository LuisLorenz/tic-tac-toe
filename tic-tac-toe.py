import random
import time

# easy player
user_player = 'X'
computer_player = 'O'

# board 
def print_board(): 
    rows = 3
    cols = 3
    board = [(('|   |   |   |')) for _ in range(rows)]
    for row in board:
        print(row)

# board w/ indices 
def print_index_board():
    rows = 3
    cols = 3
    index_board = [(f'| {i*cols} | {i*cols+1} | {i*cols+2} |') for i in range(rows)]
    for row_2 in index_board:
        print(row_2)

# check winner
def check_winner(board, player):
    
    # check rows 
    for row in range(rows):
        if all([board[row * cols + col] == player for col in range(cols)]):
            return True
    
    # check columns
    for col in range(cols):
        if all([board[row * cols + col] == player for row in range(rows)]):
            return True
   
    # check diagonals 
    if all([board[i] == player for i in [0, 4, 8]]):
        return True
    if all([board[i] == player for i in [2, 4, 6]]):
        return True
    return False

# empty spots list
empty_spots = [] 
    # list that keeps the spots[i] that are free 
    # each time an empty spots gets exchanges through a player letter the spot[i] gets removed from that list

# comuter move (probably a __init__(self) would the best choice for efficient code (level 2))

def valid_move():
    if user_move in empty_spots():
        return True
    else:
        return False 
        print('Your input was invalid. Please try again!')

def computer_move():
    move = random.choice(empty_spots)

def user_move(): 
    user_move = int(input('Make a move: '))
    if valid_move(user_move) == True:
    # at this point I want to exchange the empty spot w/ the i(user_move) in board() 
        board[user_move] = user_player

    else: 
        pass 








# intro 
introduction_text ='''
Welcome to TIC! TAC! TOE!
'''

# while game loop 
full_board = False
check_winner = False 

while full_board == False and check_winner == False: 
    print_board()
    print('')
    print_index_board()
    print('')
    move_player_1 = input('Make a move: ')

    