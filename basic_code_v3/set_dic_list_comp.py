# https://realpython.com/list-comprehension-python/

# set comprehension
quote = "life, uh, finds a way"
vowels = {char for char in quote if char in "aeiou"}
print(vowels)
    # {'e', 'u', 'a', 'i'}
    # {'i', 'a', 'e', 'u'}
    # {'a', 'e', 'u', 'i'}

    # no particular order
    # no doubled elements

# dictionary comprehension
var = {number: number * number for number in range(10)}
print(var)
    # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# walrus operator
import random
def get_weather_data():
   return random.randrange(90, 110)


var = [temp for _ in range(20) if (temp := get_weather_data()) >= 100]
print(var)
    # [100, 109, 100, 107, 103, 104, 107, 108, 105, 102, 105, 100, 101, 106]

    # the temp var is created and called 