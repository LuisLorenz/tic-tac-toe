import random
import time

# defining board 
rows = 3
cols = 3

board = [' '.join(['|__|'] * cols) for _ in range(rows)]

def print_board(): 
    for row in board:
        print(row)

print_board()
