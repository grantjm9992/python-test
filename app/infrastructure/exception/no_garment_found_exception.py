from fastapi import HTTPException
from app.infrastructure.exception.base_exception import BaseException

class NoGarmentFoundException(BaseException):
    def __init__(self):
        name='test'
        code=404