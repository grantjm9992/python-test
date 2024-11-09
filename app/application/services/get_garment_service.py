from typing import List, Optional
from app.infrastructure.response.garment_response import GarmentResponse
from app.domain.repositories.garment_repository_interface import IGarmentRepository
from app.infrastructure.api.v1.dtos.garments.garment_search import GarmentSearch
from app.infrastructure.database.query_params.garment_search_query_params import GarmentSearchQueryParams

class GetGarmentService:
    def __init__(self, repository: IGarmentRepository):
        self.repository = repository

    async def search_garments(
        self,
        search_dto: GarmentSearch
    ) -> List[GarmentResponse]:

        query_params = GarmentSearchQueryParams(
            query_params=search_dto
        )

        garments = await self.repository.find_by_query(
            query_params.query_params,
            search_dto.limit is not None and search_dto.offset is not None,
            search_dto.limit,
            search_dto.offset
        )
        return garments
