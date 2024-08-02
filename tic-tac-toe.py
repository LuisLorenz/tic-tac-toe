import random
import time

# defining board 
rows = 3
cols = 3

board = [' '.join(['|__|'] * cols) for _ in range(rows)]

def print_board(): 
    for row in board:
        print(row)

print_board() # with a function I can get same code!

introduction_text ='''
Welcome to TIC! TAC! TOE!
'''
# while loop
    # board is empty == True 
    # winner == False 

full_board = False
winner = None 

while full_board == False and winner == None: 
    print_board
    move_player_1 = input('Make a move: ')