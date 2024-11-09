from slowapi import Limiter
from slowapi.util import get_remote_address

class LimiterProvider:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.limiter = Limiter(key_func=get_remote_address)
        return cls._instance

    def get_limiter(self):
        return self.limiter
