from typing import List, Dict, Any
from src.core.models import DNSQueryResult

class LatencyProfiler:
    @staticmethod
    def rank_resolvers(results: List[DNSQueryResult]) -> List[Dict[str, Any]]:
        sorted_res = sorted([r for r in results if r.success], key=lambda x: x.latency_ms)
        return [
            {"name": r.resolver_name, "ip": r.resolver_ip, "latency_ms": r.latency_ms}
            for r in sorted_res
        ]
