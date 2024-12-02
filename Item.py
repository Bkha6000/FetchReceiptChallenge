from pydantic import BaseModel
class Item(BaseModel):
    shortDescription: str
    price: str
