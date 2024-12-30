from pydantic import BaseModel
from typing import List

class AggregatedItem(BaseModel):
  # square footage
  squareFootage: int
  # lot size sq ft
  lotSizeInAcres: float = None
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
class ThirdPartyItem1(BaseModel):
  # square footage
  squareFootage: int
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
  SquareFootage: int
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
  provider_1: List[AggregatedItem]
  provider_2: List[AggregatedItem]