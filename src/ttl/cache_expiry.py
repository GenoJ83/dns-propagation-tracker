import time
from typing import Dict, Any

class TTLExpiryModel:
    @staticmethod
    def estimate_seconds_remaining(observed_at: float, ttl: int) -> int:
        elapsed = time.time() - observed_at
        return max(0, int(ttl - elapsed))
