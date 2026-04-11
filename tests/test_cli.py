from src.cli.main import build_parser, main

def test_cli():
    p = build_parser()
    opts = p.parse_args(["google.com", "--type", "MX", "--format", "json"])
    assert opts.domain == "google.com"
    assert opts.type == "MX"
    assert opts.format == "json"
    assert main(["--version"]) == 0
