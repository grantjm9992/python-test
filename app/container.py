from dependency_injector import containers, providers
from app.core.logging.logger import Logger
from app.domain.repositories.garment_repository_interface import IGarmentRepository
from app.infrastructure.database.mongo_connection import MongoConnection
from app.infrastructure.database.repositories.garment_repository import GarmentRepository
from app.application.services.get_garment_service import GetGarmentService
import os


logger = Logger()


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["app.infrastructure.api.v1.garments.search_garments"])

    db = providers.Singleton(
        MongoConnection,
        uri=os.getenv("DATABASE_URL", "mongodb://mongo:27017"),
        db_name=os.getenv("DATABASE_NAME", "intelistyle_db")
    )

    garment_repository = providers.Factory(
        GarmentRepository,
        connection=db
    )

    garment_repository_interface = providers.Factory(
        IGarmentRepository,
        connection=db
    )

    garment_service = providers.Factory(
        GetGarmentService,
        repository=garment_repository
    )


