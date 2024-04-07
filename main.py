from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templates
import requests
import yaml

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/js", StaticFiles(directory="templates/js"), name="js") 
app.mount("/css", StaticFiles(directory="templates/css"), name="css") 


BASE_URL = "https://api.odcloud.kr/api"
with open('where-is-clothes-boxes.yaml','r') as f:
    OPEN_API_KEY = yaml.load(f, yaml.FullLoader)['options']['env'][0]['value']


@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/seongdong-gu")
async def seongdong_gu(request: Request):
    url = BASE_URL + "/15126958/v1/uddi:b8d0dfd5-cefa-4cb2-8d35-fc6b5f2507b0"  \
        + f"?serviceKey={OPEN_API_KEY}&perPage=10&page=1"
    totalCount = requests.get(url).json()['totalCount']
    url = BASE_URL + "/15126958/v1/uddi:b8d0dfd5-cefa-4cb2-8d35-fc6b5f2507b0"  \
        + f"?serviceKey={OPEN_API_KEY}&perPage={totalCount}"
    response = requests.get(url).json()['data']
    return response

if __name__ =="__main__":
    pass