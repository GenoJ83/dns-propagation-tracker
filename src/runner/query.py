import time
from typing import List
from src.core.models import DNSResolver, DNSQueryResult

class DNSQuerySimulator:
    def __init__(self, simulated_records: List[str] = None, latency_ms: float = 18.5):
        self.records = simulated_records or ["93.184.216.34"]
        self.latency_ms = latency_ms
        
    def query(self, resolver: DNSResolver, domain: str, record_type: str = "A") -> DNSQueryResult:
        return DNSQueryResult(
            resolver_name=resolver.name,
            resolver_ip=resolver.ip,
            domain=domain,
            record_type=record_type,
            records=list(self.records),
            latency_ms=self.latency_ms,
            success=True
        )
