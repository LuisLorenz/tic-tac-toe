user_input = input('num 0-8: ')

## How would you convert a number from 0 to 8 into a row and column index?
# using a for loop: 

rows = 3
cols = 3
board_list = [[' ' for x in range(cols)] for y in range(rows)]
print(board_list)

empty_spots = [] 
for row in range(rows): 
         for col in range (cols): 
            if board_list[row][col] == ' ':
                empty_spots.append((row, col))

## ideas
# enumerate the init_list 
# user_number is assigned to a free spot -> then place X/O 
# this spot leave then the empty_spots_list 
# however, it is easier to access the list through the coordinates for updating 
# how can I assign numbers to the coordinates? -> enumerate()?



