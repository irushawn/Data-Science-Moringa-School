"""
FastAPI App and the routes to be used
"""

from fastapi import FastAPI
from models import Item
from crud import create_item, read_items, read_item, update_item, delete_item

app = FastAPI()
# localhost: 127.0.0.1:8000
@app.post("/items/") # 127.0.0.1:8000/items/
def create(item: Item):
    return create_item(item)

@app.get("/items/")
def get_all_items():
    return read_items()

@app.get("/items/{item_id}")
def get_an_item(item_id: int):
    return read_item(item_id)

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return update_item(item_id, item)

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return delete_item(item_id)

