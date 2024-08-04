import random
import time

# defining board 
rows = 3
cols = 3

board = [(('|   |   |   |')) for _ in range(rows)]

def print_board(): 
    for row in board:
        print(row)

rows = 3
cols = 3

# Erzeugen des Spielfeldes mit Indizes
index_board = [(f'| {i*cols} | {i*cols+1} | {i*cols+2} |') for i in range(rows)]

def print_index_board():
    for row_2 in index_board:
        print(row_2)

# Spielfeld drucken


introduction_text ='''
Welcome to TIC! TAC! TOE!
'''
# while loop
    # board is empty == True 
    # winner == False 

full_board = False
winner = None 


while full_board == False and winner == None: 
    print_board()
    print('')
    print_index_board()
    print('')
    move_player_1 = input('Make a move: ')