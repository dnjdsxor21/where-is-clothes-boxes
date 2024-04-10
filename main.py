from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templates
import requests
import os 
import yaml
from supabase_db import fetch_table

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/img", StaticFiles(directory="templates/img"), name="img") 
app.mount("/js", StaticFiles(directory="templates/js"), name="js") 
app.mount("/css", StaticFiles(directory="templates/css"), name="css") 
app.mount("/json", StaticFiles(directory="templates/json"), name="json") 
app.mount("/templates", StaticFiles(directory="templates"), name="templates")


BASE_URL = "https://api.odcloud.kr/api"
# OPEN_API_KEY = os.environ['NAVER_API_KEY']

@app.get("/robots.txt", response_class=PlainTextResponse)
def get_robots_txt():
    content = """
    User-agent: *
    Allow: /
    Sitemap: http://clothes-box.site/templates/sitemap.xml
    """
    return PlainTextResponse(content=content)

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/map/{name}")
async def get_data(request: Request, name:str):
    name = name.replace('-',' ')
    data = fetch_table(name)
    # print(data)
    return data



if __name__ =="__main__":
    pass