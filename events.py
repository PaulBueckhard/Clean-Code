import random

from player import Player, HumanPlayer, Enemy

class Events:
    Enemy = Enemy
    def __init__(self, speed = 10, score = 0, max_enemies = 10, delay = 0.1):
        self.speed = speed
        self.score = score
        self.max_enemies = max_enemies
        self.delay = delay

        self.enemy_list = []

    def drop_enemies(self, screen, enemy, enemy_list):
        delay = random.random()
        if len(enemy_list) < self.max_enemies and delay < self.delay:
            x_pos = random.randint(0, screen.width - enemy.size)
            y_pos = 0
            enemy_list.append([x_pos, y_pos])

    def update_enemy_positions(self, screen, enemy_list):
        for idx, enemy_pos in enumerate(enemy_list):
            if enemy_pos[1] >= 0 and enemy_pos[1] < screen.height:
                enemy_pos[1] += self.speed
            else:
                enemy_list.pop(idx)
                self.score += 1
        return self.score

    def set_level(self):
        if self.score < 20:
            self.speed = 5
        elif self.score < 40:
            self.speed = 8
        elif self.score < 60:
            self.speed = 12
        else:
            self.speed = 15
        return self.speed