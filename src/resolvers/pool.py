from typing import List
from src.core.models import DNSResolver

PUBLIC_RESOLVERS: List[DNSResolver] = [
    DNSResolver("Cloudflare Primary", "1.1.1.1", "Global (Anycast)"),
    DNSResolver("Cloudflare Secondary", "1.0.0.1", "Global (Anycast)"),
    DNSResolver("Google Primary", "8.8.8.8", "Global (Anycast)"),
    DNSResolver("Google Secondary", "8.8.4.4", "Global (Anycast)"),
    DNSResolver("Quad9 Primary", "9.9.9.9", "Zurich / Anycast"),
    DNSResolver("OpenDNS Primary", "208.67.222.222", "San Francisco / Anycast"),
]

def get_default_resolvers() -> List[DNSResolver]:
    return list(PUBLIC_RESOLVERS)
