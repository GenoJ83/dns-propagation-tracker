from src.diff.compare import RecordDiff

def test_diff():
    add, rem = RecordDiff.compare(["1.1.1.1"], ["1.1.1.1", "2.2.2.2"])
    assert add == ["2.2.2.2"] and rem == []
