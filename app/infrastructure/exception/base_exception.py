class BaseException(Exception):

    message: str = 'Internal Sersser Error'

    def __str__(self):
        return self.message