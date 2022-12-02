from blockgame.events import Events

def test_events_attributes() -> None:
    events = Events()
    assert events.speed == 10
    assert events.score == 0
    assert events.max_enemies == 10
    assert events.delay == 0.1
