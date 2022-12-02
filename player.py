from colour import Colour

class Player:
    def __init__(self, x, y, size, colour = Colour.RED):
        self.x = x
        self.y = y
        self.size = size
        self.colour = colour

    def detect_collision(player_pos, enemy_pos, player, enemy):
        p_x = player_pos[0]
        p_y = player_pos[1]

        e_x = enemy_pos[0]
        e_y = enemy_pos[1]

        if (e_x >= p_x and e_x < (p_x + player.size)) or (p_x >= e_x and p_x < (e_x + enemy.size)):
            if (e_y >= p_y and e_y < (p_y + player.size)) or (p_y >= e_y and p_y < (e_y + enemy.size)):
                return True
        return False

class Enemy(Player):
    def __init__(self, x, y):
        super().__init__(x, y, size = 50, colour = Colour.BLUE)

class HumanPlayer(Player):
    def __init__(self, x, y):
        super().__init__(x, y, size = 50, colour = Colour.RED)