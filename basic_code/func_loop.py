def create_board(rows, cols): # 2 arguments 
    board = [] # is a list 
    for _ in range(rows):
        row = ' '.join(['|__|'] * cols) # same like the list comprehension - first the amount of columns are defined - then these columns get repeated for row times 
        board.append(row) # the row gets appended to the board list for 3 times  
    return board

def print_board(board):
    for row in board:
        print(row) # here each row is printed individually 

# Definiere die Anzahl der Reihen und Spalten
rows = 3
cols = 3

# Erstelle und drucke das Board
board = create_board(rows, cols)
print_board(board)
print(board)