from dependency_injector.wiring import inject, Provide
from fastapi import FastAPI, Request, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.core.fastapi.routes import add_routes
from app.core.fastapi.handlers import validation_exception_handler, http_exception_handler
from app.infrastructure.api.v1.garments.garments_routes import garment_router
from app.infrastructure.database.repositories.garment_repository import GarmentRepository
from app.infrastructure.exception.no_garment_found_exception import NoGarmentFoundException
from app.container import Container

app = FastAPI()
app.add_exception_handler(ValueError, validation_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)

add_routes([garment_router], app)

container = Container()
app.container = container
db = container.db()

@inject
async def startup_event(db=Provide[Container.db]):
    await db.connect()

@inject
async def shutdown_event(db=Provide[Container.db]):
    await db.disconnect()
