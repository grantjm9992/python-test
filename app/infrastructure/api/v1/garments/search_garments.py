from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, HTTPException, Query, Depends, Request
from pydantic import BaseModel
from typing import List, Optional
from app.application.services.get_garment_service import GetGarmentService
from app.container import Container
from app.core.slowapi.limiter_provider import LimiterProvider
from app.infrastructure.database.repositories.garment_repository import GarmentRepository
from app.infrastructure.api.v1.dtos.garments.garment_search import GarmentSearch
from app.infrastructure.api.v1.dependencies.garments.garment_query import parse_garment_search
from app.infrastructure.response.garment_response import GarmentResponse
from app.infrastructure.api.v1.garments import router
from app.infrastructure.exception.no_garment_found_exception import NoGarmentFoundException

limiter_provider = LimiterProvider()


@router.get(
    '/',
    response_model=List[GarmentResponse]
)
@limiter_provider.get_limiter().limit('5/minute')
@inject
async def search_garments(
    request: Request,
    search_dto: GarmentSearch = Depends(parse_garment_search),
    garment_service: GetGarmentService = Depends(Provide[Container.garment_service])
):
    try:
        return await garment_service.search_garments(
            search_dto
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
