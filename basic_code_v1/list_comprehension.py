# Definiere die Anzahl der Reihen und Spalten
rows = 3
cols = 3

# Erstelle das Board mit List Comprehensions
board = [' '.join(['|__|'] * cols) for _ in range(rows)]
    # raser the quotation marks with the join func 
    # with cols I can define the column number 
    # these columns get repeated for the num of rows 

# Drucke das Board
for row in board:
    print(row)