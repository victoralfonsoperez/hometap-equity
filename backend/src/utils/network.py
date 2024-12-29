import httpx
import os

async def fetch_from_api(url: str, params: dict = None, headers: dict = None) -> dict:
  async with httpx.AsyncClient() as client:
    # validate if headders is none, and initializes as an empty dictionary
    headers = headers or {}

    # API keys from the environment variables
    api_1_url = os.getenv("API_1_URL")
    api_2_url = os.getenv("API_2_URL")
    api_1_key = os.getenv("API_1_KEY")
    api_2_key = os.getenv("API_2_KEY")

    # adds the headers when matching the urls API
    if api_1_url in url:
      headers["X-API-KEY"] = api_1_key
    elif api_2_url in url:
      headers["X-API-KEY"] = api_2_key
    
    # get request with the url, params and headers
    response = await client.get(url, params=params, headers=headers)
    
    # raise error for bad responses
    response.raise_for_status()

    return response.json()