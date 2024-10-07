# user_input = input('num 0-8: ')

## How would you convert a number from 0 to 8 into a row and column index?
# using a for loop: 

# rows = 3
# cols = 3
# board_list = [[' ' for x in range(cols)] for y in range(rows)]
# print(board_list)

# empty_spots = [] 
# for row in range(rows): 
#          for col in range (cols): 
#             if board_list[row][col] == ' ':
#                 empty_spots.append((row, col))

## ideas
# enumerate the init_list 
# user_number is assigned to a free spot -> then place X/O 
# this spot leave then the empty_spots_list 
# however, it is easier to access the list through the coordinates for updating 
# how can I assign numbers to the coordinates? -> enumerate()?

# solution: calculating the coordinates simply with divion and modulus 

## calculating coordinates

x = 5 
y = 2
z = 7

# | 0 | 1 | 2 |
# | 3 | 4 | 5 |
# | 6 | 7 | 8 |

def get_row(x): 
     row = x // 3 # getting the result rounded down always
     return row 

print(get_row(x))
print(get_row(y))
print(get_row(z))
# 1
# 0
# 2

# getting row works 

## getting column 
x = 3 
y = 2
z = 7
def get_col(x):
     col = x % 3 # returning the remainder 
     return col 
    # 5 % 3 = 2 ->  col 2
    # 7 % 3 = 1 -> col 1 ...

print(get_col(x))
print(get_col(y))
print(get_col(z))
# 0
# 2
# 1

## get_coordinates

def get_coordinates(x): 
    row = x // 3 
    col = x % 3 
    return row, col

user_number = int(input('0-8'))
print('user_number')
print(get_coordinates(user_number))

# function works, yeah 