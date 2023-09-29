from fastapi import FastAPI, BackgroundTasks, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from main import run_report_generator
from path import project_folder

app = FastAPI()

app.mount("/static", StaticFiles(directory="src/api/static"), name="static")

report_folder = Jinja2Templates(
    directory=f"{project_folder}/src/view_pages/report"
)

ui_folder = Jinja2Templates(
    directory=f"{project_folder}/src/view_pages/user_interface"
)


test  =0

class Item(BaseModel):
    country: str
    league: str
    team: str


@app.get("/")
async def root():
    return {"Usage": "go to /docs"}


@app.get("/request", response_class=HTMLResponse)
async def form(request: Request):
    context = {"title": "Minha Página", "content": "Bem-vindo à minha página."}
    return ui_folder.TemplateResponse("index.html", {"request": request, "context": context})


@app.get("/report", response_class=HTMLResponse)
async def generate_report_endpoint(
        request: Request,
        bt: BackgroundTasks,
        country: str = Query(...),
        league: str = Query(...),
        team: str = Query(...),

):
    item = Item(country=country, league=league, team=team)

    run_report_generator(item.country, item.league, item.team)
    context = {"title": "Minha Página", "content": "Bem-vindo à minha página."}
    return report_folder.TemplateResponse("report.html", {"request": request, "context": context})

# @app.get("/report", response_class=HTMLResponse)
# async def generate_report_endpoint(item: Item, bt: BackgroundTasks):
#     run_report_generator(item.country, item.league, item.team)
#     report = report_folder.TemplateResponse("report.html", {"item": item})
#     return report


@app.get("/team_json")
async def generate_report_endpoint(item: Item, bt: BackgroundTasks):
    return run_report_generator(item.country, item.league, item.team)
