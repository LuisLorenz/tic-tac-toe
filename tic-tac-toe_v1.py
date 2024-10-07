import random
import time

## board w/ indices 
def print_index_board():
    rows = 3
    cols = 3
    index_board = [(f'| {i*cols} | {i*cols+1} | {i*cols+2} |') for i in range(rows)]
    for row_2 in index_board:
        print(row_2)
            # | 0 | 1 | 2 |
            # | 3 | 4 | 5 |
            # | 6 | 7 | 8 |
    print('')

    # Do you want to play again?: y/ny
    # | - | x | o |
    # | x | o | x |
    # | o | - | - |

    # | 0 | 1 | 2 |
    # | 3 | 4 | 5 |
    # | 6 | 7 | 8 |

# It's x's turn.
# Make a move (number from 0-8): 

# init board
rows = 3
cols = 3
board_list = [[' ' for x in range(cols)] for y in range(rows)]
# print(board_list) # [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']] 
# access first list with i (row)
# access sec. list with j (col) 
# coordinates (i/j) (row/col) 

## empty spots list 
empty_spots = [] 
    # list that keeps the spots[i] that are free 
    # each time an empty spots gets exchanged through a player letter the spot[i] gets removed from that list
    # e.g.: X > i = 7 
        # X[7] & board[7] gets removes from empty_spots[] 
        # empty_sport[... i = 0,1,2,3,4,5,6,8]
def reset_empty_spots_list(): 
    for row in range(rows): 
            for col in range (cols): 
                if board_list[row][col] == ' ':
                    empty_spots.append((row, col)) # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# each time a spot gets used I can simply remove that coordinate form that empyt_spots_list 
# this code runs only once in the beginning but it must be run for each move
# better simply remove exactely the move from the empty_spots list

# check winner
def check_winner(board_list, player): 
    rows = 3
    cols = 3

    # check rows 
        # 0/1,2,3
        # 1/1,2,3
        # 2/1,2,3
    for row in range(rows): 
        if all(board_list[row][col] == player for col in range(cols)):
            # here the all() is includes the changing value from col -> 0/1,2,3
            return True

    # check columns
        # 1,2,3/0
        # 1,2,3/1
        # 1,2,3/2
    for col in range(cols):
        if all([board_list[row][col] == player for row in range(rows)]):
            return True
   
    # check diagonals 
    if all([board_list[row][col] == player for row, col in [(0,0),(1,1),(2,2)]]):
        return True
    elif all([board_list[row][col] == player for row, col in [(0,2),(1,1),(2,0)]]):
        return True
    else: 
        return False

## formating board_list 
def formated_board_list(): 
    for x in board_list:
        formated_board_string = '| ' + ' | '.join(x) + ' |'
        print(formated_board_string)
    print('')

# number x -> row_x / col_x 
def get_coordinates(num_input): 
    row = num_input // 3 
    col = num_input % 3 
    return row, col

# when winner = False & empyt_spots[] has still elements > ... 

num_list = [0,1,2,3,4,5,6,7,8]
def get_valid_num(num_input):
    if num_input in num_list: 
        return True 
    else:
        return False 

def valid_move(num_input): 
    row, col = get_coordinates(num_input)
    if board_list[row][col] == ' ': # test this code 
        return True
    else:
        return False 
        print('Your chosen spot is not empty. Please try again.')

def user_move(player): 
    while True:
        user_num = int(input('Make a move (number from 0-8): ')) 
        if get_valid_num(user_num) == True:
            if valid_move(user_num) == True:
            # at this point I want to exchange the empty spot w/ the i(user_move) in board() 
                row, col = get_coordinates(user_num) 
                    # calling the values and storing them in var 
                    # getting them outside for the sub func
                board_list[row][col] = player
                empty_spots.remove((row, col))
                break
            # print(board_list)
                # do not print the board_list but the actual board 
                # therefore I have to format the board_list to the format of the actual board 

            else: 
                print('This spots is already taken. Please try again.')
        else: 
            print('Your input number was invalid. Please try again.')

    # looping move question until the valid move = True 
        # while valid == False: 
            # ... 
            #     ...
            #         valid = True 
            #         try out break

def filled_board_list():
    rows = 3
    cols = 3 
    for row in range(rows): 
        for col in range(cols): 
            if board_list[row][col] == ' ':
                board_list[row][col] = '-'
    formated_board_list()


def full_board(board_list):
    # when there are no ' ' in board_list return True 
    # for nested for loop that goes through all options (row, col)
    rows = 3
    cols = 3 
    for row in range(rows): 
        for col in range(cols): 
            if board_list[row][col] == ' ': # test this code 
                return False
                break
    return True  

def reset_board():
    rows = 3
    cols = 3 
    for row in range(rows): 
        for col in range(cols): 
            board_list[row][col] = ' '

x_wins = 0
o_wins = 0

def game():
    global x_wins, o_wins

    reset_board()
    reset_empty_spots_list()

    # while game loop 
    player = 'x'
    winner_player = None
    

    # game loop 
    while True: 
        formated_board_list()
        print_index_board()
        print(f"It's {player}'s turn.")
        user_move(player)
        if check_winner(board_list, player) == True: 
            winner_player = player 
            break
        if full_board(board_list) == True:
            tie = True 
            break
        if player == 'x':
            player = 'o'
        else: 
            player = 'x' 


    filled_board_list()
    if winner_player == 'x':  
        x_wins +=1   
        print(f'The winner is {winner_player}.') 
    elif winner_player == 'o':
        o_wins +=1  
        print(f'Sorry, you lost. The winner is {winner_player}.')
    elif tie == True: 
        print("It's a tie.")

    print(f'''Wins:
    x: {x_wins}
    o: {o_wins}
            ''')
    return x_wins, o_wins

# intro ...
introduction_text ='''
Welcome to TIC! TAC! TOE!
'''
print(introduction_text)

# choose mode
    # 1) player vs player 
    # 2) player vs random computer player 
    # 3) player vs AI 
    # 4) random computer player vs AI 
    # 5) random computer player vs random computer player / for visual represenation

game()

while True: 
    play_again = input('Do you want to play again? (y/n): ')
    if play_again == 'y':
        # init_board()
        game()
    elif play_again == 'n':
        break 
    else:
        print('Your input was invalid. Please try again.')

