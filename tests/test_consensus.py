from src.consensus.scorer import ConsensusScorer
from src.core.models import DNSQueryResult

def test_consensus_calculation():
    r1 = DNSQueryResult("R1", "1.1.1.1", "ex.com", "A", ["1.2.3.4"], 10.0)
    r2 = DNSQueryResult("R2", "8.8.8.8", "ex.com", "A", ["1.2.3.4"], 10.0)
    r3 = DNSQueryResult("R3", "9.9.9.9", "ex.com", "A", ["5.6.7.8"], 10.0)
    score = ConsensusScorer.calculate_consensus([r1, r2, r3])
    assert score == 66.67
