# oriantation board 
#     |0| |1| |2|
#     |3| |4| |5|
#     |6| |7| |8|

rows = 3
cols = 3

board = [' '.join(['|__|'] * cols) for _ in range(rows)]

def index_board():
    for i in range(len(board)):
        board[i] = f'| {i} |'

def print_board(): 
    for row in board:
        print(row)

def print_index_board(): 
    for row in index_board:
        print(row)

print_index_board()

# print_board()

# indexing 

list = ['A', 'B', 'C', 'D', 'E']
# print(list[1]) # B 

# for i in list:
#     # print(x)
#     # A
#     # B
#     # C
#     # D
#     # E
#     print(i)

for i in range(len(list)):
    print(i)
    list[i] = f'| {i} |'
    # 0
    # 1
    # 2
    # 3
    # 4
print(list) # [0, 1, 2, 3, 4]
    # ['| 0 |', '| 1 |', '| 2 |', '| 3 |', '| 4 |']


