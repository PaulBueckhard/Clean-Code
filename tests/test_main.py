import sys
import pygame
from pynput.keyboard import Key, Controller

from blockgame.screen import Screen
from blockgame.player import HumanPlayer

keyboard = Controller()

pygame.init()

screen = Screen()

def main_game_mock(player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x -= player.size
            elif event.key == pygame.K_RIGHT:
                player.x += player.size

def press_right_key():
    keyboard.press(Key.right)
    keyboard.release(Key.right)

def press_left_key():
    keyboard.press(Key.left)
    keyboard.release(Key.left)
      
def test_main_move_right() -> None:
    player = HumanPlayer(screen.width / 2, screen.height - 100)
    press_right_key()
    main_game_mock(player)
    assert player.x == 450

def test_main_move_right_twice() -> None:
    player = HumanPlayer(screen.width / 2, screen.height - 100)
    press_right_key()
    press_right_key()
    main_game_mock(player)
    assert player.x == 500

def test_main_move_left() -> None:
    player = HumanPlayer(screen.width / 2, screen.height - 100)
    press_left_key()
    main_game_mock(player)
    assert player.x == 350

def test_main_move_left_twice() -> None:
    player = HumanPlayer(screen.width / 2, screen.height - 100)
    press_left_key()
    press_left_key()
    main_game_mock(player)
    assert player.x == 300