# The enumerate function in Python adds a counter to an iterable and returns it as an enumerate object
# This can be useful when you need both the index and the value from a list or other iterable.

mylist = ['apples', 'bananas', 'cherries']
mylist_v2 = [1,2,3]

enumerated_mylist = enumerate(mylist)
print(enumerated_mylist)
# <enumerate object at 0x1026792b0>
# the enumeration must be first converted into a list or you have to iterate through it to make it readable 

# Convert to list
print(list(enumerate(enumerated_mylist)))
# [(0, (0, 'apples')), (1, (1, 'bananas')), (2, (2, 'cherries'))] # strange look because of double enumeration 

print(list(enumerate(mylist_v2)))
# [(0, 1), (1, 2), (2, 3)]

# Or iterate through it
for i, x in enumerate(mylist_v2):
    print(i, x)
# 0 1
# 1 2
# 2 3


# def create_empty_board():
#     return [' ' for _ in range(9)]

# def get_empty_positions(board):
#     return [i for i, x in enumerate(create_empty_board) if x == ' '] # if x == ' ': the condition 

# print(get_empty_positions)

empty_board = [' ' for _ in range(9)]
print(list(enumerate(empty_board)))
# (0, ' '), (1, ' '), (2, ' '), (3, ' '), (4, ' '), (5, ' '), (6, ' '), (7, ' '), (8, ' ')]

for i, x in enumerate(empty_board):
    print(i, x)
    # 0  
    # 1  
    # 2  
    # 3  
    # 4  
    # 5  
    # 6  
    # 7  
    # 8  

empty_board_v2 = ['|   |   |   |' for _ in range(3)]
print(list(enumerate(empty_board_v2)))
# (0, '|   |   |   |'), (1, '|   |   |   |'), (2, '|   |   |   |')]

for i, x in enumerate(empty_board_v2):
    print(i, x)
# 0 |   |   |   |
# 1 |   |   |   |
# 2 |   |   |   |

list_v3 = [i for i, x in enumerate(empty_board_v2) if x == ' ']
print(list(list_v3)) 
# []
print(list_v3)  
# []

# why is this the output? 
food_basic_list = ['apple', 'banana', 'strawberry', 'X', 'X', 'X', 'X', 'O']
food_list = ['a fruit' for x in food_basic_list]
print(food_list) # ['a fruit', 'a fruit', 'a fruit']
food_list = ['a fruit' for i, x in enumerate(food_basic_list)]
print(food_list) # ['a fruit', 'a fruit', 'a fruit']
food_list = ['a fruit' for i, x in enumerate(food_basic_list) if x == 'apple']
print(food_list) # ['a fruit']
food_list = ['a fruit' for i, x in enumerate(food_basic_list) if x == 'X']
print(food_list)
