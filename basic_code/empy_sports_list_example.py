# my board
    # | 0 | 1 | 2 |
    # | 3 | 4 | 5 |
    # | 6 | 7 | 8 |

# create a list with all spots[i]
    # maybe an alogrithm that goes through the board list[] > checks for ' ', gives them an indice and add them to new list

# init list - first approach

# board_list = [(' ' for i in range(0,9))]
# print(board_list) > failed

# nested loop 
rows = 3
cols = 3
board_list = [[' ' for x in range(cols)] for y in range(rows)]
print(board_list) # [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# updating the list w/ x or o
# format: board_list[row][col] = 'X'  # or 'O'
# this approach is possible because the board list is a nested list containing 3 sub lists in one super list
# first I choose the row (which sub list I want to target), next I choose the column (which element in the chosen sublist I want to target)
# board_list[1][1] = 'X'
# print(board_list)

# change the board by user input
## mapping out the board_list from 0 to 8 
    # enumerate each ' ' with index 
# row = 8
# col = 8 
# enumerated_list = [x for x in board_list[row][col]]
# print (enummerated_list)

# enumerated_list = [enumerate([x for board_list[row][col]]for row in range(rows) for col in range (cols))]
# print (enumerated_list)

for row in range(rows):
        for col in range (cols):              
            enumerated_list = enumerate(board_list[row][col])
    
print (enumerated_list)

You're close! However, enumerate should be used to get both the index and the value. Also, you should store the enumerated values in a list. Here's a hint: you can create a list of tuples where each tuple contains the index and the corresponding board position.

How would you modify your code to store these tuples in a list?

# That sounds like a good plan! 
# Assigning numbers to each spot and then asking the player to choose a spot is a clear way to handle user input. 
# How would you go about mapping the numbers 0 to 8 to the corresponding row and column indices on the board?

player_move = input('Choose a spot: ') # number 