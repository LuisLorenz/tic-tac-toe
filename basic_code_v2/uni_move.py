# __init__(self)
class z:
    def __init__(self, x, y):
        self._x = x
        self._y = y

 

# player move
def move(assigned_player, player): 
    if assigned_player == 'user':  
        while True:
            player_num = int(input('Make a move (number from 0-8): ')) 
            if get_valid_num(player_num) == True:
                if valid_move(player_num) == True:
                    row, col = get_coordinates(player_num) 
                    board_list[row][col] = player
                    empty_spots.remove((row, col))
                    break

                else: 
                    print('This spots is already taken. Please try again.')
            else: 
                print('Your input number was invalid. Please try again.')
    if assigned_player == 'computer': 
        player_num = random.choice(empty_spots) # random number 0-8 that is available 
        row, col = get_coordinates(player_num) 
        board_list[row][col] = player
        empty_spots.remove((row, col))

# game 
x_wins = 0
o_wins = 0
def game():
    global x_wins, o_wins

    reset_board()
    reset_empty_spots_list()

    # game loop 
    assigned_player = 'user'
    player = 'x'
    while True: 
        formated_board_list()
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