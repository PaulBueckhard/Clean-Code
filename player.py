RED = (255,0,0)
BLUE = (0,0,255)

class Player:
    def __init__(self, x, y, size, colour = RED):
        self.x = x
        self.y = y
        self.size = size
        self.color = colour

class Enemy(Player):
    def __init__(self, x, y):
        super().__init__(x, y, size = 50, colour = BLUE)

class HumanPlayer(Player):
	def __init__(self, x, y):
		super().__init__(x, y, size = 50, colour = RED)