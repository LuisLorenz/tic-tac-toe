cities = ["Austin", "Tacoma", "Topeka", "Sacramento", "Charlotte"]
var = {city: [0 for _ in range(7)] for city in cities}
print(var)
    # {'Austin': [0, 0, 0, 0, 0, 0, 0], 
    # 'Tacoma': [0, 0, 0, 0, 0, 0, 0], 
    # 'Topeka': [0, 0, 0, 0, 0, 0, 0], 
    # 'Sacramento': [0, 0, 0, 0, 0, 0, 0], 
    # 'Charlotte': [0, 0, 0, 0, 0, 0, 0]}

    # city names are invidual keys 

# readability
# harder
matrix = [
     [0, 0, 0],
     [1, 1, 1],
     [2, 2, 2],
]

var = [number for row in matrix for number in row]
print(var)
# [0, 0, 0, 1, 1, 1, 2, 2, 2]

# readability
# easier
matrix = [
    [0, 0, 0],
    [1, 1, 1],
    [2, 2, 2],
]
flat = []
for row in matrix:
    for number in row:
        flat.append(number)
print(flat)
# [0, 0, 0, 1, 1, 1, 2, 2, 2]

