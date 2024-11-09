from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, HTTPException, Query, Depends
from pydantic import BaseModel
from typing import List, Optional
from app.container import Container
from app.infrastructure.database.repositories.garment_repository import GarmentRepository
from app.infrastructure.api.v1.dtos.garments.garment_search import GarmentSearch
from app.infrastructure.api.v1.dependencies.garments.garment_query import parse_garment_search
from app.application.services.get_garment_service import GetGarmentService
from app.infrastructure.response.garment_response import GarmentResponse
from app.infrastructure.api.v1.garments import router
from app.infrastructure.exception.no_garment_found_exception import NoGarmentFoundException

@router.get(
    '/',
    response_model=List[GarmentResponse]
)
@inject
async def search_garments(
    search_dto: GarmentSearch = Depends(parse_garment_search),
    garment_service: GetGarmentService = Depends(Provide[Container.garment_service])
):
    """ TODO - Error/Exception handling """
    """ TODO - QueryParams """
    """ TODO - Pagination """
    try:
        results = await garment_service.search_garments(
            search_dto
        )

        if not results:
            raise HTTPException(status_code=404, detail='No garments found')
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
