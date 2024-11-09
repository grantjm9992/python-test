from app.infrastructure.database.mongo_connection import MongoConnection
from typing import List, Optional, Dict
from app.domain.entities.garment import Garment
from app.domain.repositories.garment_repository_interface import IGarmentRepository
from pymongo.errors import PyMongoError

class GarmentRepository(IGarmentRepository):
    def __init__(self, connection: MongoConnection):
        self.connection = connection
        self.db = None

    async def connect(self):
        if self.db is None:
            self.db = await self.connection.connect()

    async def find_by_query(self, query: Dict, pagination = False, limit = 0, offset = 0) -> List[Garment]:
        await self.connect()
        builder = self.db.garments.find(query)
        if (pagination == True):
            builder.skip(offset).limit(limit)
        garment_docs = await builder.to_list(length=None)
        return [Garment(**doc) for doc in garment_docs]
