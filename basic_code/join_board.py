# Definiere die Anzahl der Reihen und Spalten
rows = 3
cols = 3

# Erstelle das Board mit der join Methode
row = ' '.join(['|__|'] * cols) # one row is defined 
board = '\n'.join([row] * rows) # simply a new row is insert after each new item row -> also easy to understand 

# Drucke das Board
print(board)