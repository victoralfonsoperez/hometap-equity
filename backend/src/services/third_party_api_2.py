from src.utils.network import fetch_from_api
from src.models.api_model import ThirdPartyItem1, ThirdPartyItem2
from typing import List

# TODO generate a util to manipulate the size data

class ThirdPartyAPI2Service:
  @staticmethod
  # TODO normalize the response an model for the response
  async def get_items_from_api(url:str, params: dict = None) -> List[ThirdPartyItem1]:
    data = await fetch_from_api(url, params)
    result=data["data"]

    normalized_data = ThirdPartyItem1(
      squareFootage=result["SquareFootage"],
      #TODO pass the result["LotSizeAcres"] 
      lotSizeSqFt=0,
      yearBuilt=result["YearConstructed"],
      propertyType=result["PropertyType"],
      bedrooms=result["Bedrooms"],
      bathrooms=result["Bathrooms"],
      roomCount=result["RoomCount"],
      septicSystem=result["SepticSystem"],
      salePrice=result["SalePrice"]
    )

    return [normalized_data]