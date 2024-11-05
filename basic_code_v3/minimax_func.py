# https://www.youtube.com/watch?v=8ext9G7xspg&t=721s
# algorithm 
# consists of a minimizer and maximizer concept
# I try to maximize my win while my opponent trys to minimize his loss
# going through all the moves 
# finding best moves
# utility func 
    # measurement of how valuable the result in the tree is

# utility value
    # 'Nutzen' 
    # should be positive for me
    # formula: utility: 1 * 3 = 3     
        # winning in as little steps as possible -> 3 steps 
        # taking remaining spots: '2' + '1' to get a positive value?
        # the more the board is filled already the more moves have been made then long it takes to get to the win
        # so, it is desirable to win with an unfilled board as possible 
        # win has more value 
        # more options left 
        # always the last board is reviewed in a path: win, loss or draw of me

        # '1 *' or '-1 *'
            # differentiate who the winner was
            # so when the opponent has won it is always times '-1' 

        # draw
            # it is times '0' 

# alternating between maximizer and minimizer
    # move: player = x -> maximizer
    # last empty space = no option of choice
    # move: player = o -> minimizer
        # we want to minimize the value that 'o' has 
        # so we calculate we the smarted opponent!
        # -3 -> best choice for opponent 
