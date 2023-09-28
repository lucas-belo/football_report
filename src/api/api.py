from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel

from main import run_report_generator

app = FastAPI()


class Item(BaseModel):
    country: str
    league: str
    team: str


@app.get("/")
async def root():
    return {"Usage:": "go to /docs"}


@app.get("/report_generator")
async def generate_report_endpoint(item: Item, bt: BackgroundTasks):
    return run_report_generator(item.country, item.league, item.team)

