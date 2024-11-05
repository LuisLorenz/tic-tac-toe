# removing outlier data
    # 'Ausreißer'

# sample = [4, 5, 7, 6, -12, 4, 42]

# sample.remove(min(sample))
# sample

# sample.remove(max(sample))
# sample

# select min/max and then remove it


# list building
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# [min(x) for x in matrix]
# [1, 4, 7]

# [max(x) for x in matrix]
# [3, 6, 9]


# clipping values to the edge / interval 
    # place number between upper and lower limit
    # when the number is larger than the upper limit 
    #   then it gets transformed to the upper limit instead
    # vice versa 

# Clip values to the largest interval's edge

# upper = 100
# numbers = [42, 78, 200, -230, 25, 142]

# [min(number, upper) for number in numbers]
# [42, 78, 100, -230, 25, 100]
# the min() compares number and upper limit and choose always the smaller number
# when we have '200' in this case '100' is smaller and printed out as upper limit

# Clip values to the smallest interval's edge

# lower = 10
# numbers = [42, 78, 200, -230, 25, 142]

# [max(number, lower) for number in numbers]
# [42, 78, 200, 10, 25, 142]

# Clipping values to 10 - 100 / combi 

# lower, upper = 10, 100
# numbers = [42, 78, 100, -230, 25, 142]

# [max(min(number, upper), lower) for number in numbers]
# [42, 78, 100, 10, 25, 100]
# first numb is compared to '100' 
# -> 98 
# 98 is compared with 10 
# -> 98 

# 110 > 100
# -> 100 
# 100 > 10 
# -> 100

# 9 < 100
# -> 9 
# 9 < 10
# -> 10 

# same func in numpy with 'clip()' 


# finding closest points 
# Cartesian points (Koordinatensystem)

# import math

# point_pairs = [
#     ((12, 5), (9, 4)),
#     ((2, 5), (3, 7)),
#     ((4, 11), (15, 2))
# ]

# min(point_pairs, key=lambda points: math.dist(*points))
# ((2, 5), (3, 7))
# Euclidean distance (fly route from on point to the next)
# lambda is needed for the math operation ... (more an intermediate topic)

# lambda...: https://realpython.com/python-lambda/


# identify cheap/expensive products
# prices = {
#    "banana": 1.20,
#    "pineapple": 0.89,
#    "apple": 1.57,
#    "grape": 2.45,
# }

# min(prices.items(), key=lambda item: item[1])
# ('pineapple', 0.89)

# max(prices.items(), key=lambda item: item[1])
# ('grape', 2.45)


# finding coprime integer numb 
# def are_coprime(a, b):
#     for i in range(2, min(a, b) + 1):
#         if a % i == 0 and b % i == 0:
#             return False
#     return True

# are_coprime(2, 3)
# True 
# are_coprime(2, 4)
# False