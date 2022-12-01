import pygame

from colour import Colour

class Screen:
    def __init__(self, width = 800, height = 600, background_colour = Colour.BLACK, font_type = "monospace", font_size = 35, clock_tick = 30):
        self.width = width
        self.height = height
        self.background_colour = background_colour
        self.screen = pygame.display.set_mode((width, height))
        self.font = pygame.font.SysFont(font_type, font_size)
        self.clock = pygame.time.Clock()
        self.clock_tick = clock_tick