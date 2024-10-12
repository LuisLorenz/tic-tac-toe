# tic-tac-toe

## basic code
- generally, cut all the fancy stuff for the beginning - biggest learnings from challengening foundational code
 
- def board 
    - 2 dimensional with chaining two range functions 
    - going for a list comprehension 

- oriantation board: 
    | 0 | 1 | 2 |
    | 3 | 4 | 5 |
    | 6 | 7 | 8 |

- in progress: def rules
    - ...
    - challenge of this project (logic counter)



- playstlye 1: player vs dumb computer
    - computer chooses simply a random position each time

- playstyle 2: player vs unbeatable AI

- playstyle 3: computer vs unbeatable AI 

- use the advantage of __init__(self)



## pseudocode
- ok: board 
- ok: orientation board

- input("Make a move: ") 
    - while valide_user_input == False: 
        - empty place -> True 
        - not in range -> False
        - not empty -> False 

- ok: check if player has won 

- defining player
    - assigning X or O to a player 
    - ask user if he wants to play as X or O 

- alternating between player after each move

...

## checklist
- [x] basic board
- [x] basic board with indices for orientation
- [x] checking algorithm for winner
- [x] valid move check structure
- [x] create empty_spots list 
- [x] create user player move: challenge: transfer input player into a coordinate for checking valid move
- [x] check number 0-8 with a list ... 
- [x] format board_list into the format for the actual board 
    - join.x(y) 
        - '|' + 'X' + ' | ' + 'X' + ' | ' + 'X' + ' |' 
    - print each row with x in range(0,2) 
- [x] check valid move (coordinates) with empty list: update this list
- [x] Alternate player moves 
- [x] Assign player symbole to player_name - tell which players turn it is -> keep it simple 
- [x] implement check_winner func 
- [x] implement ending text & print final board 
- [x] fixing check winner bugs
- [x] create full_board_check 
- [x] formating board list to '-' all the empty spots
- [x] create a score board 
- [x] resetting board_list when playing another time 
    - simply access every cooridnate and set every spot to ' ' 
- [x] implement player vs player 
- [x] creating v2 with less notes for other play modes

## v2
- [x] o-player shall be asigned to the computer, x regular player 
    - at this point it would be more effecient to reuse the code by making it more universal (__init__(self)?)
- [x] adapt the info output
- [x] variation option to player vs player 
    - it is the turn of x_player, user
    - more efficient something like a class x_player
        - symbole: 'x' 
        - assigned player: 'user' 
- [ ] debug: random player can exchange filled spots
- [ ]
- [ ]
- [ ]
- [ ]
- [ ]
- [ ]
- [ ]
- [ ]



## upgrades
- [ ] last move should be filled out automatically because it is fix concering a player move 
- [ ] create an unbeatable computer AI 




