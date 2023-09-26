from fastapi import FastAPI
from pydantic import BaseModel

from main import run_report_generator

app = FastAPI()


class Item(BaseModel):
    country: str
    league: str
    team: str


@app.get("/")
async def root():
    return {"Message": "Testing"}


@app.get("/report_generator")
async def generate_report_endpoint(item: Item):
    run_report_generator(item.country, item.league, item.team)
    return "Report generated!"

