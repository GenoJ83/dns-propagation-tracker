from typing import List
from src.core.models import DNSQueryResult

class TerminalTable:
    @staticmethod
    def format_results(results: List[DNSQueryResult]) -> str:
        h_res = "RESOLVER"
        h_ip = "IP"
        h_stat = "STATUS"
        h_lat = "LATENCY"
        lines = [f"{h_res:<22} | {h_ip:<16} | {h_stat:<8} | {h_lat:<10} | RECORDS"]
        lines.append("-" * 75)
        for r in results:
            status = "OK" if r.success else "FAIL"
            records_str = ", ".join(r.records) if r.records else "none"
            lines.append(f"{r.resolver_name:<22} | {r.resolver_ip:<16} | {status:<8} | {r.latency_ms:>7.1f} ms | {records_str}")
        return "\n".join(lines)
