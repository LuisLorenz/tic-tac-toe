class player:
    def __init__(self, symbol, type):
        self.symbol = symbol
        self.type = type

user_player = player('x', 'user')
print(user_player.symbol, user_player.type)
# x user

computer_player = player('o', 'computer')
print(computer_player.symbol, computer_player.type)
# o computer

x_player = player('x', 'user')
o_player = player('o', 'computer')
print(x_player.symbol + ' and ' + x_player.type)
print(o_player.symbol + ' as well as ' + o_player.type)