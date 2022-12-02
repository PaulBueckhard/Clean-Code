import pygame

from blockgame.colour import Colour

class Screen:
    def __init__(self, width = 800, height = 600, background_colour = Colour.BLACK, font_type = "monospace", font_size = 35, clock_tick = 30):
        self.width = width
        self.height = height
        self.background_colour = background_colour
        self.screen = pygame.display.set_mode((width, height))
        self.font = pygame.font.SysFont(font_type, font_size)
        self.clock = pygame.time.Clock()
        self.clock_tick = clock_tick

    def refresh_background(self):
        self.screen.fill(self.background_colour)

    def draw_enemies(self, enemy_list, enemy):
        for enemy_pos in enemy_list:
            pygame.draw.rect(self.screen, Colour.BLUE, (enemy_pos[0], enemy_pos[1], enemy.size, enemy.size))

    def draw_player(self, player, player_pos):
        pygame.draw.rect(self.screen, Colour.RED, (player_pos[0], player_pos[1], player.size, player.size))

    def draw_score_label(self, score, colour = Colour.YELLOW):
        text = f"Score: {score}"
        label = self.font.render(text, 1, colour)
        self.screen.blit(label, (self.width - 200, self.height - 40))

    def update_screen(self, enemy_list, player, score, enemy, player_pos):
        self.refresh_background()
        self.draw_enemies(enemy_list, enemy)
        self.draw_player(player, player_pos)
        self.draw_score_label(score)
        
        self.clock.tick(self.clock_tick)
        pygame.display.update()