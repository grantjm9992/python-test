class BaseException(Exception):

    message: str = 'Internal Server Error'

    def __str__(self):
        return self.message