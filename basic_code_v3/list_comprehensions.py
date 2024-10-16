# for loop -> list 
squares = []
for number in range(10):
     squares.append(number * number)

print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# map -> list
prices = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08
def get_price_with_tax(price):
     return price * (1 + TAX_RATE)


final_prices = map(get_price_with_tax, prices)
final_prices
# map object at 0x7f34da341f90>

print(list(final_prices))
# [1.1772000000000002, 25.4448, 62.467200000000005, 4.9248, 7.322400000000001]

# iterable and func are stored in map()
# results are stored there
