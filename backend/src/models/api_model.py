from pydantic import BaseModel
from typing import List

class ThirdPartyItem1(BaseModel):
  # square footage
  squareFoorage: int
  # lot size sq ft
  lotSizeSqFt: int = None
  # year built
  yearBuilt: int
  # property type
  propertyType: str
  # bedrooms
  bedrooms: int
  # bathrooms
  bathrooms: int
  # room count
  roomCount: int
  # septic system
  septicSystem: bool
  # sale price
  salePrice: int

class ThirdPartyItem2(BaseModel):
  # square footage
  SquareFoorage: int
  # lot size acres
  LotSizeAcres: float
  # year built
  YearConstructed: int
  # property type
  PropertyType: str
  # bedrooms
  Bedrooms: int
  # bathrooms
  Bathrooms: int
  # room count
  RoomCount: int
  # septic system
  SepticSystem: bool
  # sale price
  SalePrice: int

class AggregatedResponse(BaseModel):
  source_1_items: List[ThirdPartyItem1]
  source_2_items: List[ThirdPartyItem2]