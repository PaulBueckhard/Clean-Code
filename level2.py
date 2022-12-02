import pygame

from player import HumanPlayer
from screen import Screen
from events import Level2
from main import play_game

if __name__ == "__main__":
	pygame.init()

	screen = Screen()
	player = HumanPlayer(screen.width / 2, screen.height - 100)
	events = Level2()

	play_game(screen, player, events)