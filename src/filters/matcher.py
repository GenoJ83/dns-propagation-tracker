from typing import List

def match_expected(actual_records: List[str], expected_records: List[str]) -> bool:
    return set(actual_records) == set(expected_records)
