from blockgame.colour import Colour

class Player:
    def __init__(self, x, y, size, colour = Colour.RED):
        self.x = x
        self.y = y
        self.size = size
        self.colour = colour

class Enemy(Player):
    def __init__(self, x, y):
        super().__init__(x, y, size = 50, colour = Colour.BLUE)

class HumanPlayer(Player):
    def __init__(self, x, y):
        super().__init__(x, y, size = 50, colour = Colour.RED)