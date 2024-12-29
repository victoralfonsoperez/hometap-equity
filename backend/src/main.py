from fastapi import FastAPI
from src.controllers.item_controller import router as item_router

app = FastAPI()

# Include the item router
app.include_router(item_router)