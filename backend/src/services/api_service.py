from src.services.third_party_api_1 import ThirdPartyAPI1Service
from src.services.third_party_api_2 import ThirdPartyAPI2Service
from src.models.api_model import AggregatedResponse
import os

class APIService:
  @staticmethod
  async def aggregate_items(search_query: dict = None) -> AggregatedResponse:
    # API urls from env variables
    url_1 = os.getenv("API_1_URL")
    url_2 = os.getenv("API_2_URL")

    # fetch items from thirdpartys
    source_2_items = await ThirdPartyAPI2Service.get_items_from_api(url_2, params=search_query)
    source_1_items = await ThirdPartyAPI1Service.get_items_from_api(url_1, params=search_query)

    # aggregated data
    return AggregatedResponse(provider_1=source_1_items, provider_2=source_2_items)