import json
from typing import Dict, Any
from src.core.models import DNSQueryResult

def export_json(summary: Dict[str, Any]) -> str:
    # serialize DNSQueryResult objects
    cleaned = dict(summary)
    cleaned["results"] = [
        {"resolver": r.resolver_name, "ip": r.resolver_ip, "records": r.records, "latency_ms": r.latency_ms}
        for r in summary["results"]
    ]
    return json.dumps(cleaned, indent=2)
