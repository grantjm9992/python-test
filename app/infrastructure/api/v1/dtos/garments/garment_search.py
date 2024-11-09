from pydantic import BaseModel, Field, root_validator
from typing import Optional, List

class GarmentSearch(BaseModel):
    product_title: Optional[str] = Field(None)
    product_categories: Optional[List[str]] = Field(None)
    size: Optional[str] = Field(None)
    min_price: Optional[float] = Field(None)
    max_price: Optional[float] = Field(None)
    limit: Optional[int] = Field(None)
    offset: Optional[int] = Field(None)

    @root_validator(pre=True)
    def transform_product_categories(cls, values):
        if isinstance(values.get('product_categories'), str):
            values['product_categories'] = values['product_categories'].split(',')
        return values