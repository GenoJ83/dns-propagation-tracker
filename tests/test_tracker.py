from src.tracker import DNSPropagationTracker

def test_tracker_audit():
    tracker = DNSPropagationTracker()
    audit = tracker.audit("example.com")
    assert audit["domain"] == "example.com"
    assert audit["total_resolvers"] >= 5
    assert audit["fully_propagated"] is True
