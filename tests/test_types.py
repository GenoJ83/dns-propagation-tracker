from src.records.types import is_valid_type

def test_record_types():
    assert is_valid_type("A") is True
    assert is_valid_type("mx") is True
    assert is_valid_type("UNKNOWN") is False
