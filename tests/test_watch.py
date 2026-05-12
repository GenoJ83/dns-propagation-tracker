from src.watch.monitor import PropagationWatchSession

def test_watch_session():
    session = PropagationWatchSession(target_consensus=90.0, max_attempts=3)
    assert session.record_attempt(50.0) is False
    assert session.record_attempt(95.0) is True
