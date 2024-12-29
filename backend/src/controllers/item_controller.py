from fastapi import APIRouter
from src.services.service import get_item_data
from src.models.item_model import Item

router = APIRouter()

@router.get("/home_equity", response_model=Item)
async def get_item():
    # Call the service to get the item data
    return get_item_data()