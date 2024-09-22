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
        print(row) # 1x row equals one element in the board list = one row

# board w/ indices 
def print_index_board():
    rows = 3
    cols = 3
    index_board = [(f'| {i*cols} | {i*cols+1} | {i*cols+2} |') for i in range(rows)]
    for row_2 in index_board:
        print(row_2)
            # | 0 | 1 | 2 |
            # | 3 | 4 | 5 |
            # | 6 | 7 | 8 |

# check winner
def check_winner(board, player): 
    
    # var
    rows = 3
    cols = 3

    # check rows 
    for row in range(rows): # 0,1,2 
        if all([board[row * cols + col] == player for col in range(cols)]): # 0,1,2 
            # 3 options
            # 0 + 0 = X 
            # 1) X[0] X[1] X[2] for one row
            # 2) X[3] X[4] X[5]
            # 3) X[6] X[7] X[8]
            return True

    # check columns
    for col in range(cols):
        if all([board[row * cols + col] == player for row in range(rows)]):
            # options
                # 1) X[0] X[3] X[6] 
                # 2) X[1] X[4] X[7]
                # 3) X[3] X[5] X[8]
            # row: switching makes not sense because each option is in one row
            # col: 0,1,2 
                # board[row*cols+ col] == x for row in range(rows)
                    # col is right: 0,1,2 
                    # row*cols
                        # 0
                        # 3
                        # 6 
            return True
   
    # check diagonals 
    if all([board[i] == player for i in [0, 4, 8]]):
        # only one option for this diagonal 
        return True
    if all([board[i] == player for i in [2, 4, 6]]):
        return True
    return False

# init board
rows = 3
cols = 3
board_list = [[' ' for x in range(cols)] for y in range(rows)]
print(board_list) # [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']] 
# access first list with i (row)
# access sec. list with j (col) 
# coordinates (i/j) (row/col) 

# empty spots list 
empty_spots = [] 
    # list that keeps the spots[i] that are free 
    # each time an empty spots gets exchanged through a player letter the spot[i] gets removed from that list
    # e.g.: X > i = 7 
        # X[7] & board[7] gets removes from empty_spots[] 
        # empty_sport[... i = 0,1,2,3,4,5,6,8]
for row in range(rows): 
         for col in range (cols): 
            if board_list[row][col] == ' ':
                empty_spots.append((row, col)) # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# each time a spot gets used I can simply remove that coordinate form that empyt_spots_list 

# number x -> row_x / col_x 
def get_coordinates(x): 
    row = x // 3 
    col = x % 3 
    return row, col

# when winner = False & empyt_spots[] has still elements > ... 
def valid_move(): 
    ## check valide number
        # also check that the input was an int from 0 - 8 
        # therefore I can check if user_move is in the list[0, 1, ... , 8]
        # false -> try again

    get_coordinates(user_move)
    if board_list[row][col] == ' ': # test this code 
        return True
    else:
        return False 
        print('Your chosen spot is not empty. Please try again.')

   
def computer_move():
    move = random.choice(empty_spots)

def user_move(): 
    user_move = int(input('Make a move (number from 0-8): ')) 
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

for x in range
    print(hello)