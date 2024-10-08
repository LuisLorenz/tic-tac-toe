import random
import time

# index board 
def print_index_board():
    rows = 3
    cols = 3
    index_board = [(f'| {i*cols} | {i*cols+1} | {i*cols+2} |') for i in range(rows)]
    for row_2 in index_board:
        print(row_2)
    print('')

# init board_list
rows = 3
cols = 3
board_list = [[' ' for x in range(cols)] for y in range(rows)]

# empty spots list 
empty_spots = [] 
def reset_empty_spots_list(): 
    for row in range(rows): 
            for col in range (cols): 
                if board_list[row][col] == ' ':
                    empty_spots.append((row, col)) 

# check winner
def check_winner(board_list, player): 
    rows = 3
    cols = 3

    # check row
    for row in range(rows): 
        if all(board_list[row][col] == player for col in range(cols)):
            return True

    # check col 
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

# formating board_list 
def formated_board_list(): 
    for x in board_list:
        formated_board_string = '| ' + ' | '.join(x) + ' |'
        print(formated_board_string)
    print('')

# number to coordinates 
def get_coordinates(num): 
    row = num // 3 
    col = num % 3 
    return row, col

# get valid number
num_list = [0,1,2,3,4,5,6,7,8]
def get_valid_num(num):
    if num in num_list: 
        return True 
    else:
        return False 

# get valid move
def valid_move(num): 
    row, col = get_coordinates(num)
    if board_list[row][col] == ' ': 
        return True
    else:
        return False 
        print('Your chosen spot is not empty. Please try again.')

# player move
def move(assigned_player, player): 
    if assigned_player == 'user':  
        while True:
            num = int(input('Make a move (number from 0-8): ')) 
            print('')
            if get_valid_num(num) == True:
                if valid_move(num) == True:
                    row, col = get_coordinates(num) 
                    board_list[row][col] = player
                    empty_spots.remove((row, col))
                    break

                else: 
                    print('This spots is already taken. Please try again.')
            else: 
                print('Your input number was invalid. Please try again.')
    if assigned_player == 'computer': 
        # random number 0-8 that is available 
            
        row, col = random.choice(empty_spots) 
        board_list[row][col] = player
        empty_spots.remove((row, col))

# fill empyt spots
def filled_board_list():
    rows = 3
    cols = 3 
    for row in range(rows): 
        for col in range(cols): 
            if board_list[row][col] == ' ':
                board_list[row][col] = '-'
    formated_board_list()

# check full board
def full_board(board_list):
    rows = 3
    cols = 3 
    for row in range(rows): 
        for col in range(cols): 
            if board_list[row][col] == ' ': 
                return False
                break
    return True  

# reset board
def reset_board():
    rows = 3
    cols = 3 
    for row in range(rows): 
        for col in range(cols): 
            board_list[row][col] = ' '

# game 
x_wins = 0
o_wins = 0
game_mode = None
x_player = None
o_player = None

def choose_game_mode(): 
    game_mode = int(input('''Choose your game mode: 
    0: player vs player
    1: player vs random computer
    2: player vs AI 
    3: random computer vs AI
    -> mode: '''))
    print('')
    if game_mode == 0: 
        o_player = 'user'
    elif game_mode == 1:
        o_player = 'computer'
    elif game_mode == 2: 
        o_player = 'AI'
    elif game_mode == 3: 
        x_player = 'computer'
        o_player = 'AI'
    else:
        print('Your input was invalid. Please try again.')

def game(game_mode):
    global x_wins, o_wins

    reset_board()
    reset_empty_spots_list()

    # game loop 
    player = 'x'
    assigned_player = 'user'
    while True: 
        time.sleep(0.3)
        formated_board_list()
        time.sleep(0.3)
        if assigned_player == 'user':
            print_index_board()
            print(f"It's {player}'s turn.")
        move(assigned_player, player)
        if check_winner(board_list, player) == True: 
            winner_player = player 
            break
        if full_board(board_list) == True:
            tie = True 
            break
        if player == 'x':
            player = 'o'
            assigned_player = 'computer'
        else: 
            player = 'x' 
            assigned_player = 'user'

    filled_board_list()

    # track wins 
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
choose_game_mode()
game(game_mode)

# super game loop 
while True: 
    play_again = input('Do you want to play again? (y/n): ')
    if play_again == 'y':
        game(game_mode)
    elif play_again == 'n':
        break 
    else:
        print('Your input was invalid. Please try again.')

