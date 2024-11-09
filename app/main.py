from dependency_injector.wiring import inject, Provide
from fastapi import FastAPI, Request
from app.core.fastapi.routes import add_routes
from app.infrastructure.exception.base_exception import BaseException
from app.infrastructure.api.v1.garments.garments_routes import garment_router
from app.infrastructure.database.repositories.garment_repository import GarmentRepository
from app.container import Container
import logging

app = FastAPI()
add_routes([garment_router], app)

container = Container()
app.container = container
db = container.db()

@app.exception_handler(BaseException)
async def unicorn_exception_handler(request: Request, exc: BaseException):
    return JSONResponse(
        status_code=exc.code,
        content={"message": f"{exc.name}"},
    )

@app.on_event("startup")
async def startup_event():
    await db.connect()


@app.on_event("shutdown")
@inject
async def shutdown_event(container: Container = Provide[Container.db]):
    await db.disconnect()
