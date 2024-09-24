
rows = 3
cols = 3
board_list = [[' ' for x in range(cols)] for y in range(rows)]
print(board_list)

empty_spots = [] 
    # list that keeps the spots[i] that are free 
    # each time an empty spots gets exchanged through a player letter the spot[i] gets removed from that list
    # e.g.: X > i = 7 
        # X[7] & board[7] gets removes from empty_spots[] 
        # empty_sport[... i = 0,1,2,3,4,5,6,8]
for row in range(rows): 
         for col in range (cols): 
            if board_list[row][col] == ' ':
                empty_spots.append((row, col))

def get_coordinates(num_input): 
    row = num_input // 3 
    col = num_input % 3 
    return row, col

def valid_move(num_input): 
    row, col = get_coordinates(num_input)
    if board_list[row][col] == ' ': # test this code 
        return True
    else:
        return False 
        # print('Your chosen spot is not empty. Please try again.')


user_num = int(input('Make a move (number from 0-8): '))
print(valid_move(user_num))
# always True