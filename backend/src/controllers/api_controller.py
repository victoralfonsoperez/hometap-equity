from fastapi import APIRouter, HTTPException, Query
from src.services.api_service import APIService
from src.models.api_model import AggregatedResponse

router = APIRouter()

@router.get("/home_equity", response_model=AggregatedResponse)
async def get_aggregated_items(search_query: str = Query("", min_length=1, max_length=100)):
  """
  Endpoint to fetch aggregated data item from the thirdparty APIs
  - search query: String to filter the results
  """
  try:
    # calls the service to aggregate data from the APIs
    aggregated_response = await APIService.aggregate_items(search_query=search_query)

    return aggregated_response
  except Exception as e:
    # exception handler
    raise HTTPException(status_code=500, detail=f"Error aggregating items: {str(e)}")