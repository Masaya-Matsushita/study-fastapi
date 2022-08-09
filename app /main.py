from typing import Optional
from fastapi import FastAPI
# from pydantic import BaseModal

# class Item(BaseModal):
#     name: str
#     description: Optional[str]
#     price: int
#     tax: Optional[float]

app = FastAPI()

@app.get("/")
def foo():
    return {"message": "hello world"}

# @app.post("/item/")
# def create_item(item: Item):
#     return item
