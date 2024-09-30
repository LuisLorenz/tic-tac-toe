
rows = 3
cols = 3
board_list = [[' ' for x in range(cols)] for y in range(rows)]
# print(board_list)

def formated_board_list(): 
    for x in board_list:
        y = ' | '.join(x)
        # [' ', ' ', ' ']
        # [' ', ' ', ' ']
        # [' ', ' ', ' ']
        
        # first step
            #   |   |  
            #   |   |  
            #   |   |  
        print(y)

# join func
    # my_list = ['X', 'Y']
    # formated_list = ' | '.join(my_list)
    # print(formated_list)


formated_board_list()


