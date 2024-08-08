# rows = 3
# cols = 3
# board = [(('|   |   |   |')) for _ in range(rows)]

# def print_board(): 
#     for row in board:
#         print(row)

# changed_board = [' x ' for '|   |   |   |' in board]
# def print_changed_board(): 
#     for row in changed_board:
#         print(row)

# creating frame board
def print_board():
    rows = 3
    cols = 3
    board = [('|   |   |   |') for _ in range(rows)]
    for row in board:
        print(row)

# creating 9 elements (empty spots)
def create_empty_board():
    return [' ' for _ in range(9)]

# creating indices for board
    # board serves as frame 
def print_board_with_indices(board):
    for i in range(0, 9, 3): # 0 - 3 - 6
        print(f'| {board[i]} | {board[i+1]} | {board[i+2]} |')

# Erstelle die Liste der leeren Bereiche
def get_empty_positions(board):
    return [i for i, x in enumerate(board) if x == ' ']

# Main-Programm
# if __name__ == "__main__":
#     board = create_empty_board()
#     print_board_with_indices(board)
#     empty_positions = get_empty_positions(board)
#     print("Leere Positionen:", empty_positions)

print_board()
