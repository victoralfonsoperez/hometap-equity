from src.utils.size import square_feet_to_acres
from src.utils.network import fetch_from_api
from src.models.api_model import ThirdPartyItem1, AggregatedItem
from typing import List

class ThirdPartyAPI1Service:
  @staticmethod
  async def get_items_from_api(url:str, params: dict = None) -> List[AggregatedItem]:
    data = await fetch_from_api(url, params)
    
    result=data["data"]

    normalized_data = AggregatedItem(
      squareFootage=result["squareFootage"],
      # lot size in acres
      lotSizeInAcres=square_feet_to_acres(result["lotSizeSqFt"]),
      yearBuilt=result["yearBuilt"],
      propertyType=result["propertyType"],
      bedrooms=result["bedrooms"],
      bathrooms=result["bathrooms"],
      roomCount=result["features"]["roomCount"],
      septicSystem=result["features"].get("septicSystem", False),
      salePrice=result["lastSalePrice"]
    )

    return [normalized_data]