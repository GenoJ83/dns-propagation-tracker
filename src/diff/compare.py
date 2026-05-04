from typing import List, Tuple

class RecordDiff:
    @staticmethod
    def compare(old_records: List[str], new_records: List[str]) -> Tuple[List[str], List[str]]:
        added = [r for r in new_records if r not in old_records]
        removed = [r for r in old_records if r not in new_records]
        return added, removed
