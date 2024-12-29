from pydantic import BaseModel

class Item(BaseModel):
    price: int
    name: str
    size: int