import pygame

from player import HumanPlayer
from screen import Screen
from events import Level3
from main import play_game

if __name__ == "__main__":
	pygame.init()

	screen = Screen()
	player = HumanPlayer(screen.width / 2, screen.height - 100)
	events = Level3(max_enemies = 15) 

	play_game(screen, player, events)