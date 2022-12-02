import pygame
import random
import sys

from player import Enemy, HumanPlayer
from screen import Screen
from events import Events

pygame.init()

screen = Screen()
events = Events()

player = HumanPlayer(screen.width / 2, screen.height - 100)
enemy = Enemy(random.randint(0, screen.width), 0)

player_pos = [player.x, player.y]
enemy_pos = [enemy.x, enemy.y]

enemy_list = []

game_over = False

def collision_check(enemy_list, player_pos):
	for enemy_pos in enemy_list:
		if detect_collision(enemy_pos, player_pos):
			return True
	return False

def detect_collision(player_pos, enemy_pos):
	p_x = player_pos[0]
	p_y = player_pos[1]

	e_x = enemy_pos[0]
	e_y = enemy_pos[1]

	if (e_x >= p_x and e_x < (p_x + player.size)) or (p_x >= e_x and p_x < (e_x+enemy.size)):
		if (e_y >= p_y and e_y < (p_y + player.size)) or (p_y >= e_y and p_y < (e_y+enemy.size)):
			return True
	return False

while not game_over:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:

			x = player_pos[0]
			y = player_pos[1]

			if event.key == pygame.K_LEFT:
				x -= player.size
			elif event.key == pygame.K_RIGHT:
				x += player.size

			player_pos = [x,y]

	screen.refresh_background()

	events.drop_enemies(screen, enemy, enemy_list)

	events.update_enemy_positions(screen, enemy_list)

	events.set_level()

	if collision_check(enemy_list, player_pos):
		game_over = True
		break

	screen.update_screen(enemy_list, player, events.score, enemy, player_pos)