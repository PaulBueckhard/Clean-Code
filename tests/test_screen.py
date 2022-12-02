import pygame

from blockgame.screen import Screen

def test_screen_attributes() -> None:
    pygame.init()
    screen = Screen()
    assert screen.width == 800
    assert screen.height == 600
    assert screen.background_colour == (0,0,0)
    assert screen.clock_tick == 30

def test_screen_refresh_background() -> None:
    pygame.init()
    screen = Screen()
    screen.refresh_background()
    assert screen.screen == pygame.display.set_mode((800, 600))