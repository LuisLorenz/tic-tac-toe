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

# building the sum with a list comprehension
value = sum([number * number for number in range(1000)])
print(value) 
# 332833500

# calculating with large numbers
# here a list comprehension is a bad choice
    # each individual value is stored in a list which results as in huge list and take a lot of capacity
# for this reason switching to a generator is the better choice
    # one value gets updated and stored at a time 
# value = sum(number * number for number in range(1_000_000_000))
# print(value)
# 333333332833333333500000000

# alt with map()
# sum(map(lambda number: number * number, range(1_000_000_000)))

# timing 
import random
import timeit
TAX_RATE = .08
PRICES = [random.randrange(100) for _ in range(100_000)]
def get_price(price):
    return price * (1 + TAX_RATE)

def get_prices_with_map():
    return list(map(get_price, PRICES))

def get_prices_with_comprehension():
    return [get_price(price) for price in PRICES]

def get_prices_with_loop():
    prices = []
    for price in PRICES:
        prices.append(get_price(price))
    return prices


print(timeit.timeit(get_prices_with_map, number=100))


print(timeit.timeit(get_prices_with_comprehension, number=100))


print(timeit.timeit(get_prices_with_loop, number=100))

0.5768839580014173
0.5517941670004802
0.5881909159998031