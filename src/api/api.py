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


def sum_numbers(first, second):
    sum = first + second
    return sum


@app.get("/calc")
async def sum_numbers_endpoint(item: Item):
    sum = sum_numbers(item.first_number, item.second_number)
    return sum


@app.get("/report_generator")
async def generate_report_endpoint(item: Item):
    run_report_generator(item.country, item.league, item.team)
    return "Report generated!"

