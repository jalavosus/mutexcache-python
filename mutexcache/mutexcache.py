from threading import Lock
from expiringdict import ExpiringDict


class MutexCache:
    def __init__(self, default_ttl: int = 30):
        self._mutCache = ExpiringDict(max_len=None, max_age_seconds=default_ttl)

    def get(self, cache_key: str) -> Lock:
        lock = self._mutCache.get(cache_key)
        if not lock:
            lock = self._new_mutex(cache_key)

        return lock

    def _new_mutex(self, cache_key: str) -> Lock:
        lock = Lock()
        self._mutCache[cache_key] = lock

        return lock
