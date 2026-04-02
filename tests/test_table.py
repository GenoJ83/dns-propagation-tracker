from src.reporter.table import TerminalTable
from src.core.models import DNSQueryResult

def test_table_output():
    r = DNSQueryResult("Google", "8.8.8.8", "domain.com", "A", ["1.1.1.1"], 15.0)
    tbl = TerminalTable.format_results([r])
    assert "Google" in tbl and "8.8.8.8" in tbl and "15.0 ms" in tbl
