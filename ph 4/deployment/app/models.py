"""
We will create Pydantic Models to be used for
data validation purposes

We will create an app for managing items. The
item features will keep track of are name, price
"""
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
