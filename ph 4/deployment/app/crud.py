"""
Contain the CRUD logic
- Creating an item
- Updating an item
- Reading an item
- Reading items
- Deleting an item
"""

from fastapi import HTTPException
from models import Item

items = [] # in-built memory/db
# items = [
#     {"name": "mango",
#      "price": 50
#     },
#     {"name": "apple",
#      "price": 40
#     },
#     {"name": "matchboc",
#      "price": 10
#     },
#     {"name": "cooking oil",
#      "price": 500
#     }
# ]

def create_item(item: Item):
    items.append(item)
    return item

def read_items():
    return items

def read_item(item_id: int):
    if item_id >= len(items):
        raise HTTPException(status_code=404, detail='Item not found')
    return items[item_id] # items[0], items[1]

def update_item(item_id: int, updated_item: Item):
    if item_id >= len(items):
        raise HTTPException(status_code=404, detail='Item not found')
    items[item_id] = updated_item
    return updated_item

def delete_item(item_id: int):
    if item_id >= len(items):
        raise HTTPException(status_code=404, detail='Item not found')
    return items.pop(item_id)
