from fastapi import Query
from typing import Optional, Literal
from app.infrastructure.api.v1.dtos.garments.garment_search import GarmentSearch

def parse_garment_search(
    product_title: Optional[str] = Query(None),
    brand: Optional[str] = Query(None),
    product_categories: Optional[str] = Query(None),
    gender: Optional[Literal["men", "women"]] = Query(None),
    min_price: Optional[float] = Query(None, ge=0),
    max_price: Optional[float] = Query(None, ge=0),
    limit: Optional[int] = Query(None, gt=0),
    offset: Optional[int] = Query(None, ge=0),
) -> GarmentSearch:
    product_categories_list = product_categories.split(",") if product_categories else None

    return GarmentSearch(
        product_title=product_title,
        brand=brand,
        product_categories=product_categories_list,
        min_price=min_price,
        max_price=max_price,
        gender=gender,
        limit=limit,
        offset=offset
    )
