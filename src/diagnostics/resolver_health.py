from typing import List
from src.core.models import DNSQueryResult

def find_failing_resolvers(results: List[DNSQueryResult]) -> List[str]:
    return [r.resolver_name for r in results if not r.success]
