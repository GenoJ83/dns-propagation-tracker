from typing import List, Dict, Set
from src.core.models import DNSQueryResult

class ConsensusScorer:
    @staticmethod
    def calculate_consensus(results: List[DNSQueryResult]) -> float:
        successful = [r for r in results if r.success]
        if not successful:
            return 0.0
        answers = [tuple(sorted(r.records)) for r in successful]
        counts: Dict[tuple, int] = {}
        for a in answers:
            counts[a] = counts.get(a, 0) + 1
        max_match = max(counts.values())
        return round((max_match / len(successful)) * 100.0, 2)
