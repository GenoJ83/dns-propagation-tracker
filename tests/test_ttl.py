import time
from src.ttl.cache_expiry import TTLExpiryModel

def test_ttl_remaining():
    now = time.time()
    assert TTLExpiryModel.estimate_seconds_remaining(now - 100, 300) in [199, 200]
    assert TTLExpiryModel.estimate_seconds_remaining(now - 400, 300) == 0
