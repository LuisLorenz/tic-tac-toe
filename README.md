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
- [ ] check valid move (coordinates) with empty list
- [x] check number 0-8 with a list ... 
- [ ] 

## upgrades
- [ ] last move should be filled out automatically because it is fix concering a player move 
- [ ] create an unbeatable computer AI 




