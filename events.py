from player import Enemy

class Events:
    Enemy = Enemy
    def __init__(self, speed = 10, score = 0, max_enemies = 10, delay = 0.1):
        self.speed = speed
        self.score = score
        self.max_enemies = max_enemies
        self.delay = delay

        self.enemy_list = []