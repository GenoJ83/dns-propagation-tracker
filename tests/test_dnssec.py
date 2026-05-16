from src.dnssec.checker import parse_dnssec_flags

def test_dnssec_flags():
    assert parse_dnssec_flags(0x0020) is True
    assert parse_dnssec_flags(0x0000) is False
