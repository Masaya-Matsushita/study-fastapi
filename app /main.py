from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    tax: Optional[float] = 1.0

app = FastAPI()

@app.get("/")
def foo():
    return {"message": "hello world"}

@app.post("/item/")
def create_item(item: Item):
    return {"message": f"{item.name}は、税込価格{int(item.price*item.tax)}円です。"}
