from pydantic import BaseModel, HttpUrl
from typing import Optional
from enum import Enum

class CategoryEnum(str, Enum):
    finished = "finished"
    semi_finished = "semi-finished"
    raw = "raw"

class UOMEnum(str, Enum):
    mtr = "mtr"
    mm = "mm"
    ltr = "ltr"
    ml = "ml"
    cm = "cm"
    mg = "mg"
    gm = "gm"
    unit = "unit"
    pack = "pack"

class ProductBase(BaseModel):
    name: str
    category: CategoryEnum
    description: Optional[str]
    product_image: Optional[HttpUrl]
    sku: Optional[str]
    unit_of_measure: Optional[UOMEnum]
    lead_time: Optional[int]

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductResponse(ProductBase):
    product_id: int
    created_date: str
    updated_date: str

    class Config:
        orm_mode = True
