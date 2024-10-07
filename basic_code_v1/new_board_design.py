rows = 3
cols = 3

board = [(('|   |   |   |')) for _ in range(rows)]

def print_board(): 
    for row in board:
        print(row)

print_board()

# |   |   |   |
# |   |   |   |
# |   |   |   |

# | 0 | 1 | 2 |
# | 3 | 4 | 5 |
# | 6 | 7 | 8 |

rows = 3
cols = 3

# Erzeugen des Spielfeldes mit Indizes
board = [(f'| {i*cols} | {i*cols+1} | {i*cols+2} |') for i in range(rows)]

def print_board():
    for row in board:
        print(row)

# Spielfeld drucken
print_board()