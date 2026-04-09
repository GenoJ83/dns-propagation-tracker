from src.filters.matcher import match_expected

def test_matcher():
    assert match_expected(["1.1.1.1", "2.2.2.2"], ["2.2.2.2", "1.1.1.1"]) is True
    assert match_expected(["1.1.1.1"], ["1.1.1.2"]) is False
