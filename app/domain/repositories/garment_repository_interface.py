from typing import List, Dict
from abc import ABC, abstractmethod
from app.domain.entities.garment import Garment

class IGarmentRepository(ABC):
    @abstractmethod
    async def connect(self):
        pass

    @abstractmethod
    async def find_by_query(self, query: Dict) -> List[Garment]:
        pass
