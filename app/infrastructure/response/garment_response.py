from pydantic import BaseModel
from typing import List, Optional

class GarmentResponse(BaseModel):
    product_title: str
    product_categories: Optional[list] = None
    size: Optional[str] = None
    price: Optional[float] = None