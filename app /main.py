from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/countries")
def country(country_name: Optional[str] = None, city_no: Optional[int] = None):
    return {
        "country_name": country_name,
        "city_no": city_no
    }
