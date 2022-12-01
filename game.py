import pygame
import random
import sys

from player import Enemy, HumanPlayer
from colour import Colour
from screen import Screen

pygame.init()

screen = Screen()

player = HumanPlayer(screen.width / 2, screen.height - 100)
enemy = Enemy(random.randint(0, screen.width), 0)

player_pos = [player.x, player.y]

enemy_pos = [enemy.x, enemy.y]
enemy_list = []

SPEED = 10

game_over = False

score = 0

def set_level(score, SPEED):
	if score < 20:
		SPEED = 5
	elif score < 40:
		SPEED = 8
	elif score < 60:
		SPEED = 12
	else:
		SPEED = 15
	return SPEED
	# SPEED = score/5 + 1


def drop_enemies(enemy_list):
	delay = random.random()
	if len(enemy_list) < 10 and delay < 0.1:
		x_pos = random.randint(0, screen.width - enemy.size)
		y_pos = 0
		enemy_list.append([x_pos, y_pos])

def draw_enemies(enemy_list):
	for enemy_pos in enemy_list:
		pygame.draw.rect(screen.screen, Colour.BLUE, (enemy_pos[0], enemy_pos[1], enemy.size, enemy.size))

def update_enemy_positions(enemy_list, score):
	for idx, enemy_pos in enumerate(enemy_list):
		if enemy_pos[1] >= 0 and enemy_pos[1] < screen.height:
			enemy_pos[1] += SPEED
		else:
			enemy_list.pop(idx)
			score += 1
	return score

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

	screen.screen.fill(Colour.BLACK)

	drop_enemies(enemy_list)
	score = update_enemy_positions(enemy_list, score)
	SPEED = set_level(score, SPEED)

	text = "Score:" + str(score)
	label = screen.font.render(text, 1, Colour.YELLOW)
	screen.screen.blit(label, (screen.width-200, screen.height-40))

	if collision_check(enemy_list, player_pos):
		game_over = True
		break

	draw_enemies(enemy_list)

	pygame.draw.rect(screen.screen, Colour.RED, (player_pos[0], player_pos[1], player.size, player.size))

	screen.clock.tick(screen.clock_tick)

	pygame.display.update()