from typing import List, Dict
from src.core.models import DNSResolver

def group_by_region(resolvers: List[DNSResolver]) -> Dict[str, List[DNSResolver]]:
    groups: Dict[str, List[DNSResolver]] = {}
    for r in resolvers:
        region = "Global" if "Anycast" in r.location else r.location.split("/")[0].strip()
        groups.setdefault(region, []).append(r)
    return groups
