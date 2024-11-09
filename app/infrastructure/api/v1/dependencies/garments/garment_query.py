from fastapi import Query
from typing import Optional
from app.infrastructure.api.v1.dtos.garments.garment_search import GarmentSearch

def parse_garment_search(
    product_title: Optional[str] = Query(None),
    product_categories: Optional[str] = Query(None),
    size: Optional[str] = Query(None),
    min_price: Optional[float] = Query(None),
    max_price: Optional[float] = Query(None),
    limit: Optional[int] = Query(10),
    offset: Optional[int] = Query(0),
) -> GarmentSearch:
    product_categories_list = product_categories.split(",") if product_categories else None

    return GarmentSearch(
        product_title=product_title,
        product_categories=product_categories_list,
        size=size,
        min_price=min_price,
        max_price=max_price,
        limit=limit,
        offset=offset
    )
