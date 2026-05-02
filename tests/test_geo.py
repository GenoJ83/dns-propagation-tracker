from src.geo.regions import group_by_region
from src.resolvers.pool import get_default_resolvers

def test_geo_grouping():
    resolvers = get_default_resolvers()
    groups = group_by_region(resolvers)
    assert "Global" in groups
    assert len(groups["Global"]) >= 4
