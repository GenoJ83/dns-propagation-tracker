from src.resolvers.pool import get_default_resolvers

def test_default_resolvers():
    resolvers = get_default_resolvers()
    assert len(resolvers) >= 5
    names = [r.name for r in resolvers]
    assert any("Cloudflare" in n for n in names)
    assert any("Google" in n for n in names)
