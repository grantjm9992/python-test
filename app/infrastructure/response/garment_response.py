from pydantic import BaseModel
from typing import List, Optional, Literal

class GarmentResponse(BaseModel):
    product_id: str
    product_title: str
    brand: str
    gender: Optional[Literal["men", "women"]]
    product_categories: Optional[list] = None
    size: Optional[str] = None
    price: Optional[float] = None