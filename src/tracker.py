from typing import List, Dict, Any
from src.resolvers.pool import get_default_resolvers
from src.runner.query import DNSQuerySimulator
from src.consensus.scorer import ConsensusScorer
from src.core.models import DNSQueryResult

class DNSPropagationTracker:
    def __init__(self, resolvers=None, simulator=None):
        self.resolvers = resolvers or get_default_resolvers()
        self.simulator = simulator or DNSQuerySimulator()
        
    def probe(self, domain: str, record_type: str = "A") -> List[DNSQueryResult]:
        results = []
        for res in self.resolvers:
            results.append(self.simulator.query(res, domain, record_type))
        return results
        
    def audit(self, domain: str, record_type: str = "A") -> Dict[str, Any]:
        results = self.probe(domain, record_type)
        consensus = ConsensusScorer.calculate_consensus(results)
        avg_latency = round(sum(r.latency_ms for r in results) / len(results), 2) if results else 0.0
        return {
            "domain": domain,
            "record_type": record_type,
            "total_resolvers": len(results),
            "consensus_percent": consensus,
            "avg_latency_ms": avg_latency,
            "fully_propagated": consensus == 100.0,
            "results": results
        }
