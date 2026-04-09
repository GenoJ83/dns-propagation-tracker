import argparse

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="dnstrack", description="DNS propagation auditor")
    p.add_argument("--version", action="store_true", help="Print version")
    p.add_argument("domain", nargs="?", default="example.com", help="Domain to probe")
    p.add_argument("--type", default="A", choices=["A", "AAAA", "CNAME", "MX", "TXT"], help="DNS record type")
    p.add_argument("--format", choices=["table", "json"], default="table")
    return p

def main(args=None):
    p = build_parser()
    opts = p.parse_args(args)
    if opts.version:
        print("dnstrack v0.1.0")
        return 0
    return 0
