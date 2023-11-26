from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn


class Item(BaseModel):
    item_id: int
    name: str
    description: str
    price: float
    tax: float

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item():
    return {"item": Item}

@app.post("/items/")
async def create_item(item: Item):
    return item

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8085, reload=True)