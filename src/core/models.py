from dataclasses import dataclass, field
from typing import List, Optional
import time

@dataclass
class DNSResolver:
    name: str
    ip: str
    location: str
    
@dataclass
class DNSQueryResult:
    resolver_name: str
    resolver_ip: str
    domain: str
    record_type: str
    records: List[str]
    latency_ms: float
    ttl: int = 300
    success: bool = True
    error: Optional[str] = None
