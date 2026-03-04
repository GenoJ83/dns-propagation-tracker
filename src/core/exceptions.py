class DNSTrackerError(Exception):
    """Base exception."""

class ResolverTimeoutError(DNSTrackerError):
    """Raised when upstream resolver times out."""

class InconsistentRecordsError(DNSTrackerError):
    """Raised when resolvers return conflicting answers."""
