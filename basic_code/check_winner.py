# Funktion zum Überprüfen des Siegers

def check_winner(board, player):
    # Überprüfen der Reihen
    for row in range(rows):
        if all([board[row * cols + col] == player for col in range(cols)]):
            return True
    # starting w/ the first row 
    # 0 + 0 -> 0, 1, 2 
    # 3, 4, 5
    # 6, 7, 8

# https://chatgpt.com/c/a380db1b-2c18-4443-ad2e-ac9790723763


    # Überprüfen der Spalten
    for col in range(cols):
        if all([board[row * cols + col] == player for row in range(rows)]):
            return True

    # practically [0, 3, 6], [1, 4, 7] and [2, 5, 8]
    # [row * cols + col]: indices for each col 
    # row is varies for rows total: 0, 1, 2 
    # also super: col goes through cols: 0, 1, 2
    # first: 0 + 0 -> 0, 3, 6 
    # sec: 1, 4, 7
    # third: 2, 5, 8 
    # 
    # gathering the list of indices for the first col and check it 
    # then repeat if for the next 2 col  

# check diagonals
    if all([board[i] == player for i in [0, 4, 8]]): 
        return True
        # if all board elements for the position 0. 4 and 8 are equal to the player symbole -> True -> return True 
    if all([board[i] == player for i in [2, 4, 6]]):
        return True

# returning True for the func with the latest board and the player that has its turn 