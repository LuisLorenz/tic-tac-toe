# Definiere die Anzahl der Reihen und Spalten
rows = 3
cols = 3

# Erstelle das Board mit verschachtelten Schleifen
for _ in range(rows):
    row = ''
    for _ in range(cols):
        row += '|__| ' # for each col the row gets on box 
        # the whole system repeats 2 more times 
    # print(row.strip()) 
    print(row) 