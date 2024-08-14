dimension = 9
empty_list = ['|   |' for x in range(dimension)]
print(empty_list)
new_element = 'Hello'
empty_list[1] = new_element
print(empty_list) # ['|   |', 'Hello', '|   |', '|   |', '|   |', '|   |', '|   |', '|   |', '|   |']
index = 2
empty_list[index] = 'X'
print(empty_list)
