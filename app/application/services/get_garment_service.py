from typing import List, Optional
from app.infrastructure.response.garment_response import GarmentResponse
from app.domain.repositories.garment_repository_interface import IGarmentRepository
from app.infrastructure.api.v1.dtos.garments.garment_search import GarmentSearch

class GetGarmentService:
    def __init__(self, repository: IGarmentRepository):
        self.repository = repository

    async def search_garments(
        self,
        search_dto: GarmentSearch
    ) -> List[GarmentResponse]:


        query = {}
        if search_dto.product_title:
            query["product_title"] = {"$regex": search_dto.product_title, "$options": "i"}
        if search_dto.product_categories:
            query["product_categories"] = search_dto.product_categories
        if search_dto.size:
            query["size"] = search_dto.size
        if search_dto.min_price is not None or search_dto.max_price is not None:
            query["price"] = {}
            if search_dto.min_price is not None:
                query["price"]["$gte"] = search_dto.min_price
            if search_dto.max_price is not None:
                query["price"]["$lte"] = search_dto.max_price

        garments = await self.repository.find_by_query(
            query,
            search_dto.limit is not None and search_dto.offset is not None,
            search_dto.limit,
            search_dto.offset
        )
        return garments
