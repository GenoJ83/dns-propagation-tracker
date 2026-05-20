from src.diagnostics.resolver_health import find_failing_resolvers
from src.core.models import DNSQueryResult

def test_failing_resolvers():
    r1 = DNSQueryResult("Good", "1.1.1.1", "a", "A", [], 10.0, success=True)
    r2 = DNSQueryResult("Bad", "2.2.2.2", "a", "A", [], 0.0, success=False)
    assert find_failing_resolvers([r1, r2]) == ["Bad"]
