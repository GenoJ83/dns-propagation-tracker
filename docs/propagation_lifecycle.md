# DNS Propagation Dynamics

```
Authoritative NS Update
       |
       +--> Resolver Cloudflare (TTL 300s) --> Propagated [100%]
       +--> Resolver Google (TTL 300s)     --> Propagated [100%]
       +--> Resolver Quad9 (Cached)        --> Pending    [0%]
```
