from pydantic import BaseModel, Field, root_validator, model_validator
from typing import Optional, List, Literal

class GarmentSearch(BaseModel):
    product_title: Optional[str] = Field(None)
    product_categories: Optional[List[str]] = Field(None)
    brand: Optional[str] = Field(None)
    min_price: Optional[float] = Field(None, ge=0)
    max_price: Optional[float] = Field(None, gt=0)
    gender: Optional[Literal["men", "women"]] = Field(None)
    limit: Optional[int] = Field(None, gt=0)
    offset: Optional[int] = Field(None, ge=0)
    order_by: Literal["product_title"] = "product_title"

    @model_validator(mode="before")
    def transform_product_categories(cls, values):
        if isinstance(values.get('product_categories'), str):
            values['product_categories'] = values['product_categories'].split(',')
        return values


    @model_validator(mode="before")
    def check_price_range(cls, values):
        min_price = values.get("min_price")
        max_price = values.get("max_price")

        if min_price is not None and max_price is not None:
            if max_price <= min_price:
                raise ValueError("max_price must be greater than min_price")

        return values