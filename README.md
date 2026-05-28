# dns-propagation-tracker

Multi-resolver global DNS propagation auditor, query latency profiler, and record consistency checker.

[![CI](https://github.com/GenoJ83/dns-propagation-tracker/actions/workflows/ci.yml/badge.svg)](https://github.com/GenoJ83/dns-propagation-tracker/actions)

## Features
- **Multi-Resolver Prober**: Queries top global Anycast resolvers (Cloudflare, Google, Quad9, OpenDNS)
- **Consensus Scoring**: Calculates real-time agreement percentage across distributed resolvers
- **Latency Benchmarking**: Ranks resolvers by round-trip latency
- **TTL Expiry Modeling**: Tracks cache decay and predicts propagation convergence

## Quick Start
```python
from src.tracker import DNSPropagationTracker

tracker = DNSPropagationTracker()
audit = tracker.audit('github.com', record_type='A')
print(f"Consensus: {audit['consensus_percent']}%")
print(f"Average Latency: {audit['avg_latency_ms']} ms")
```
