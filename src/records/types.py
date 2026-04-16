SUPPORTED_TYPES = ["A", "AAAA", "CNAME", "MX", "TXT", "NS", "SOA"]

def is_valid_type(record_type: str) -> bool:
    return record_type.upper() in SUPPORTED_TYPES
