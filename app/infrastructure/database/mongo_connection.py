from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
import os

class MongoConnection:
    """ TODO - Move to core/shared folder """

    def __init__(self, uri: Optional[str] = None, db_name: str = "intelistyle_db"):
        self.uri = uri or os.getenv("MONGO_URI", "mongodb://mongo:27017")
        self.db_name = db_name
        self.client: Optional[AsyncIOMotorClient] = None
        self.db = None

    async def connect(self):
        if not self.client:
            self.client = AsyncIOMotorClient(self.uri)
            self.db = self.client[self.db_name]
            print("MongoDB connection established.")
        return self.db

    async def disconnect(self):
        if self.client:
            self.client.close()
            print("MongoDB connection closed.")
