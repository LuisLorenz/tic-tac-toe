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

# print_board()

# indexing 

for i in board:
    board.append('|{i}|')

print_board(1)

