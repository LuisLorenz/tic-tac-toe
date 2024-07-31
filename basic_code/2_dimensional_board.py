# 3x1 

for x in range(0,2):
    print('|  |') # 0 and 1? 
    #|  |
    # |  |

# Definiere die Anzahl der Reihen und Spalten
rows = 3 
cols = 3

# Definiere die einzelnen Zellen
cell = '|  |'

# Erstelle eine Zeile
row = ' '.join([cell] * cols) # |  | * 3 

# Drucke das Board
for _ in range(rows): # 0, 1, 2 
    print(row)

# possbile tictactoe board 

# search for alternatives to create this board

# https://chatgpt.com/c/36d39944-26a2-4da7-a828-bd52a5c963f2
