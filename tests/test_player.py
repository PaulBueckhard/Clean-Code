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
    player_pos = [player.x, player.y]
    enemy = Enemy(400, 500)
    enemy_pos = [enemy.x, enemy.y]
    assert Player.detect_collision(player_pos, enemy_pos, player, enemy)

def test_collision_detection_based_on_size() -> None:
    player = HumanPlayer(400, 500)
    player_pos = [player.x, player.y]
    enemy = Enemy(449, 451)
    enemy_pos = [enemy.x, enemy.y]
    assert Player.detect_collision(player_pos, enemy_pos, player, enemy)