from src.tracker import DNSPropagationTracker
from src.export.json_out import export_json
from src.reporter.table import TerminalTable

def test_full_dns_audit_pipeline():
    tracker = DNSPropagationTracker()
    audit = tracker.audit("github.com", "A")
    table = TerminalTable.format_results(audit["results"])
    assert "RESOLVER" in table
    json_str = export_json(audit)
    assert "github.com" in json_str
