class PropagationWatchSession:
    def __init__(self, target_consensus: float = 100.0, max_attempts: int = 10):
        self.target_consensus = target_consensus
        self.max_attempts = max_attempts
        self.attempts = 0
        
    def record_attempt(self, current_consensus: float) -> bool:
        self.attempts += 1
        return current_consensus >= self.target_consensus or self.attempts >= self.max_attempts
