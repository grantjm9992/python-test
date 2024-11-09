class RateLimiter:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(RateLimiter, cls).__new__(cls)
            cls.instance.limiter = Limiter()
        return cls.instance

    def get_rate_limiter(self):
        return self.limiter