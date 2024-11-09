from typing import Optional
from pydantic import BaseModel, Field, validator

class Garment(BaseModel):
    product_title: str
    product_categories: Optional[list] = None
    gender: Optional[str] = None
    price: Optional[float] = Field(default=None, ge=0, description="Price of the garment, must be non-negative")

    class Config:
        orm_mode = True

    @validator("product_title")
    def validate_name(cls, value: str) -> str:
        if len(value) < 3:
            raise ValueError("Garment name must be at least 3 characters long.")
        return value
