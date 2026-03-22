from src.latency.bench import LatencyProfiler
from src.core.models import DNSQueryResult

def test_latency_rank():
    r1 = DNSQueryResult("Slow", "1.1.1.1", "ex.com", "A", [], 55.0)
    r2 = DNSQueryResult("Fast", "8.8.8.8", "ex.com", "A", [], 12.0)
    ranks = LatencyProfiler.rank_resolvers([r1, r2])
    assert ranks[0]["name"] == "Fast"
    assert ranks[1]["name"] == "Slow"
