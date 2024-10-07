def check_winner(board_list, player): 
    # this function checks the spots in the init_board

    # the board list needs two indices [row][col]
    # single numbers are converted into a coordination format 
    
    # var
    rows = 3
    cols = 3

    # check rows 
    for row in range(rows): # 0,1,2 
        if all([board_list[row * cols + col] == player for col in range(cols)]): # 0,1,2 
            # 3 options
            # 0 + 0 = X 
            # 1) X[0] X[1] X[2] for one row
            # 2) X[3] X[4] X[5]
            # 3) X[6] X[7] X[8]
            return True

    # check columns
    for col in range(cols):
        if all([board_list[row * cols + col] == player for row in range(rows)]):
            # options
                # 1) X[0] X[3] X[6] 
                # 2) X[1] X[4] X[7]
                # 3) X[3] X[5] X[8]
            # row: switching makes not sense because each option is in one row
            # col: 0,1,2 
                # board[row*cols+ col] == x for row in range(rows)
                    # col is right: 0,1,2 
                    # row*cols
                        # 0
                        # 3
                        # 6 
            return True
   
    # check diagonals 
    if all([board_list[i] == player for i in [0, 4, 8]]):
        # only one option for this diagonal 
        return True
    if all([board_list[i] == player for i in [2, 4, 6]]):
        return True
    return False