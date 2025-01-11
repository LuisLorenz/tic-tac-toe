# https://realpython.com/python-min-and-max/
# finding the smallest and largest value in an iterable 

# continue here: Getting Started With Python’s min() and max() Functions

# format
# min(iterable, *[, default, key]) -> minimum_value
# max(iterable, *[, default, key]) -> maximum_value
    # iterable: Takes an iterable object, like a list, tuple, dictionary, or string - required 
    # default: Holds a value to return if the input iterable is empty - not required
    # key: Accepts a single-argument function to customize the comparison criteria - not required 

# single arg
num_list = [3, 5, 9, 1, -5]
print(f'This is the minimum {min(num_list)} and this is the maximum {max(num_list)}.')
    # This is the minimum -5 and this is the maximum 9.

# condition for the list elements
    # all the values in the input iterable must be comparable
        # [3, "5.0", 9, 1.0, "-5"] -> error 
        # [3, 5.0, 9, 1.0, -5] -> fine 

# multi arg 
# min(arg_1, arg_2[, ..., arg_n], *[, key]) -> minimum_value
# max(arg_1, arg_2[, ..., arg_n], *[, key]) -> maximum_value
    # arg_1, arg_2, ..., arg_n: 	Accepts any number of regular arguments to compare:
        # at least 2 arg are required 
        # key: Takes a single-argument function to customize the comparison criteria: 
            # no requirements 

# min/max on strings
print(min("abcdefghijklmnopqrstuvwxyz"))

print(max("abcdefghijklmnopqrstuvwxyz"))

print(min("abcdWXYZ"))

print(max("abcdWXYZ"))
# a
# z
# W -> capital letters have a lower a value 
# d -> lower case letters has a higher value

# min/max on ASCII table 
print(min("abc123ñ"))
print(max("abc123ñ"))
# 1
# ñ

# the order is based on the unicode number
# >>> ord("A")
# 65

# >>> ord("a")
# 97

# >>> min("aA")
# 'A'

# >>> max("aA")
# 'a'

# min/max on a word list
# >>> min(["Hello", "Pythonista", "and", "welcome", "world"])
# 'Hello'

# >>> max(["Hello", "Pythonista", "and", "welcome", "world"])
# 'world'

# min/max on dictionary 
# >>> prices = {
# ...    "banana": 1.20,
# ...    "pineapple": 0.89,
# ...    "apple": 1.57,
# ...    "grape": 2.45,
# ... }


# >>> min(prices)
# 'apple'

# >>> max(prices)
# 'pineapple'

# >>> calling min/max focues just on the key this way
# alternative writing 
    # this option is clearer for the reader to understand 
# >>> min(prices.keys())
# 'apple'

# >>> max(prices.keys())
# 'pineapple'

# min/max on values of dic
# >>> min(prices.values())
# 0.89
# >>> max(prices.values())
# 2.45

# min/max on key-value pair
# >>> min(prices.items())
# ('apple', 1.57)
# >>> max(prices.items())
# ('pineapple', 2.45)
# decision: of (x1, x2), (y1, y2)
    # first comparison: x1 & y1 
        # e.g.: x1 < y1 -> max((y1, y2))
    # if x1 == y1
        # second comparison: x2 & y2 ... 
    # in the dic context the first item is always a unic key 
        # keys are never equal ... 

# using a key 
# >>> min(["20", "3", "35", "7"])
# '20'
# >>> max(["20", "3", "35", "7"])
# '7'
# >>> min(["20", "3", "35", "7"], key=int)
# '3'
# >>> max(["20", "3", "35", "7"], key=int)
# '35'

# using default
# >>> min([], default=42)
# 42
# >>> max([], default=42)
# 42
# be aware that no error is caused this way!

# combi w/ list comprehensions
# >>> letters = ["A", "B", "C", "X", "Y", "Z"]
# >>> min(letters)
# 'A'
# >>> min([letter.lower() for letter in letters])
# 'a'
# >>> max(letters)
# 'Z'
# >>> max([letter.lower() for letter in letters])
# 'z'

# list comprehension vs key
# >>> letters = ["A", "B", "C", "X", "Y", "Z"]
# >>> min([letter.lower() for letter in letters])
# 'a' 
# printout is also the transformed data, choice depends on original data
# >>> min(letters, key=str.lower)
# 'A'
# printout is the original data, choice depends on transformed data

# generator expression > list comprehension
    # each time the list comprehension run a list is created for min/max
    # this list takes memory
    # when you do not need that list in your code then choose 'gen expression' 
    # e.g.: list comp
        # min([letter.lower() for letter in letters])
    # e.g.: gen exp
        # min(letter.lower() for letter in letters)
            # no ‘[]‘ here (square brackets)
            # getting a lower case output 
    # this structure comes in use when you want to transform the data (upper/lower case) 

# https://realpython.com/python-minimax-nim/