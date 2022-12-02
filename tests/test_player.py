import pygame

from blockgame.player import Player, HumanPlayer, Enemy
from blockgame.colour import Colour

def test_player_attributes() -> None:
    player = Player(400, 500, 50, Colour.RED)
    assert player.x == 400
    assert player.y == 500
    assert player.size == 50
    assert player.colour == (255,0,0)

def test_collision_detection_same_position() -> None:
    player = HumanPlayer(400, 500)
    enemy = Enemy(400, 500)
    assert Player.detect_collision(player, enemy)

def test_collision_detection_based_on_size() -> None:
    player = HumanPlayer(400, 500)
    enemy = Enemy(449, 451)
    assert Player.detect_collision(player, enemy)

def test_collision_detection_barely_missed() -> None:
    player = HumanPlayer(400, 500)
    enemy = Enemy(450, 450)
    assert Player.detect_collision(player, enemy) == False

def test_draw_function() -> None:
    player = Player(400, 500, 50)
    screen = pygame.display.set_mode((800, 600))
    expected_result = str(pygame.draw.rect(screen, player.colour, (player.x, player.y, player.size, player.size)))
    assert expected_result == '<rect(400, 500, 50, 50)>'