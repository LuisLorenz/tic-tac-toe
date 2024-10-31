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