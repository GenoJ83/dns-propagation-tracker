def parse_dnssec_flags(flags: int) -> bool:
    # Check AD (Authenticated Data) bit: 0x0020
    return bool(flags & 0x0020)
