# oriantation board 
#     |0| |1| |2|
#     |3| |4| |5|
#     |6| |7| |8|

rows = 3
cols = 3

board = [' '.join(['|__|'] * cols) for _ in range(rows)]

def print_board(): 
    for row in board:
        print(row)

# def index_board():
#     for i in range(len(board)):
#         board[i] = f'| {i} |'



# def print_index_board(): 
#     for row in index_board:
#         print(row)



# print_board()

# indexing 

# list = ['A', 'B', 'C', 'D', 'E']
# print(list[1]) # B 

# for i in list:
#     # print(x)
#     # A
#     # B
#     # C
#     # D
#     # E
#     print(i)

# for i in range(len(list)):
#     print(i)
#     list[i] = f'| {i} |'
#     # 0
#     # 1
#     # 2
#     # 3
#     # 4
# print(list) # [0, 1, 2, 3, 4]
#     # ['| 0 |', '| 1 |', '| 2 |', '| 3 |', '| 4 |']

rows = 3
cols = 3

# Erstelle ein Board mit indizierten Feldern
board = [f'| {i} |' for i in range(rows * cols)]

def print_board():
    for i in range(rows):
        # Join the elements in the current row with a space
        row_str = ' '.join(board[i * cols:(i + 1) * cols]) # so I is  ... 
        print(row_str)

        # so definitely I need some kind of formular 

    # | 0 | | 1 | | 2 |
    # | 3 | | 4 | | 5 |
    # | 6 | | 7 | | 8 |


print_board()

# better board
    # |   |   |   |
    # |   |   |   |
    # |   |   |   |

