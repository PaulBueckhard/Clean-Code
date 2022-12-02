import sys
import pygame

from player import HumanPlayer
from screen import Screen
from events import Events

def play_game(screen, player, events):
	game_over = False
	while not game_over:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT and player.x > 0:
					player.x -= (player.size / 2)
				elif event.key == pygame.K_RIGHT and player.x < (screen.width - player.size):
					player.x += (player.size / 2)

		events.drop_enemies(screen.width)
		events.update_enemy_positions(screen.height)
		events.set_level()

		screen.update_screen(events.enemy_list, player, events.score)

		if events.collision_check(player):
			game_over = True
			break

if __name__ == "__main__":
	pygame.init()

	screen = Screen()
	player = HumanPlayer(screen.width / 2, screen.height - 100)
	events = Events()

	play_game(screen, player, events)