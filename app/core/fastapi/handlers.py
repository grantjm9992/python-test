from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

async def validation_exception_handler(request: Request, exc: ValueError):
    errors = [{"message": error["msg"], "type": error["type"]} for error in exc.errors()]
    logger.error('error')
    return JSONResponse(
        status_code=422,
        content={
            "status_code": 422,
            "detail": "Validation Error",
            "errors": errors,
        },
    )

async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status_code": exc.status_code,
            "detail": exc.detail,
        },
    )
