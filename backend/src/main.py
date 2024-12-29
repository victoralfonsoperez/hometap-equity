from fastapi import FastAPI
from src.controllers.api_controller import router as item_router
from dotenv import load_dotenv
import os

# Loading the env variables from .env file
load_dotenv()

# fetch API urls from env vars
api_1_url = os.getenv("API_1_URL")
api_2_url = os.getenv("API_2_URL")

app = FastAPI()

app.include_router(item_router)

# logs api urls to confirm they are loaded correctly
print(f"API 1 URL: {api_1_url}")
print(f"API 2 URL: {api_2_url}")