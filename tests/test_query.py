from src.runner.query import DNSQuerySimulator
from src.core.models import DNSResolver

def test_query_simulation():
    sim = DNSQuerySimulator(["192.0.2.1"], latency_ms=12.0)
    res = sim.query(DNSResolver("Test", "127.0.0.1", "Local"), "example.com")
    assert res.success is True
    assert res.records == ["192.0.2.1"]
    assert res.latency_ms == 12.0
