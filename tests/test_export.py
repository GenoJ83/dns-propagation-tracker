import json
from src.export.json_out import export_json
from src.core.models import DNSQueryResult

def test_json_export():
    r = DNSQueryResult("Res", "1.1.1.1", "ex.com", "A", ["10.0.0.1"], 20.0)
    summary = {"domain": "ex.com", "consensus_percent": 100.0, "results": [r]}
    txt = export_json(summary)
    data = json.loads(txt)
    assert data["domain"] == "ex.com"
    assert data["results"][0]["ip"] == "1.1.1.1"
