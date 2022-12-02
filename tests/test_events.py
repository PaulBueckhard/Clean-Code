from blockgame.events import Events

def test_events_attributes() -> None:
    events = Events()
    assert events.speed == 10
    assert events.score == 0
    assert events.max_enemies == 10
    assert events.delay == 0.1

def test_events_drop_enemies() -> None:
    events = Events()
    screen_width = 800
    new_enemy_list = [3]
    events.drop_enemies(screen_width)
    events.enemy_list = new_enemy_list
    assert len(events.enemy_list) == 1

def test_events_enemy_position_update() -> None:
    events = Events()
    screen_height = 600
    new_enemy_list = [3]
    events.update_enemy_positions(screen_height)
    events.enemy_list = new_enemy_list
    assert len(events.enemy_list) == 1

def test_events_set_level() -> None:
    events = Events(0, 0)
    events.set_level()
    assert events.speed == 5

    events = Events(0, 21)
    events.set_level()
    assert events.speed == 8

    events = Events(0, 41)
    events.set_level()
    assert events.speed == 12

    events = Events(0, 61)
    events.set_level()
    assert events.speed == 15