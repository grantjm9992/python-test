from dependency_injector.wiring import inject, Provide
from fastapi import FastAPI, Request, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler
from app.core.fastapi.routes import add_routes
from app.core.fastapi.handlers import validation_exception_handler, http_exception_handler
from app.infrastructure.api.v1.garments.garments_routes import garment_router
from app.infrastructure.database.repositories.garment_repository import GarmentRepository
from app.infrastructure.exception.no_garment_found_exception import NoGarmentFoundException
from app.container import Container
from app.core.slowapi.limiter_provider import LimiterProvider

app = FastAPI()
app.add_exception_handler(ValueError, validation_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
add_routes([garment_router], app)

container = Container()
app.container = container
db = container.db()

limiter_provider = LimiterProvider()
app.state.limiter = limiter_provider.get_limiter()
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@inject
async def startup_event(db=Provide[Container.db]):
    await db.connect()

@inject
async def shutdown_event(db=Provide[Container.db]):
    await db.disconnect()
