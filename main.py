from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templates
import requests
import os 
import yaml

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/js", StaticFiles(directory="templates/js"), name="js") 
app.mount("/css", StaticFiles(directory="templates/css"), name="css") 


BASE_URL = "https://api.odcloud.kr/api"
OPEN_API_KEY = os.environ['NAVER_API_KEY']


@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/seongdong-gu")
async def seongdong_gu(request: Request):
    with open('api.yaml', 'r') as f:
        api = yaml.load(f, yaml.FullLoader)['api']['seongdong-gu']
    url = BASE_URL + api  \
        + f"?serviceKey={OPEN_API_KEY}&perPage=10&page=1"
    totalCount = requests.get(url).json()['totalCount']
    url = BASE_URL + api  \
        + f"?serviceKey={OPEN_API_KEY}&perPage={totalCount}"
    response = requests.get(url).json()['data']
    return response

@app.get("/seodaemun-gu")
async def seongdong_gu(request: Request):
    with open('api.yaml', 'r') as f:
        api = yaml.load(f, yaml.FullLoader)['api']['seodaemun-gu']
    url = BASE_URL + api  \
        + f"?serviceKey={OPEN_API_KEY}&perPage=10&page=1"
    totalCount = requests.get(url).json()['totalCount']
    url = BASE_URL + api  \
        + f"?serviceKey={OPEN_API_KEY}&perPage={totalCount}"
    response = requests.get(url).json()['data']
    return response

@app.get("/dongjak-gu")
async def seongdong_gu(request: Request):
    with open('api.yaml', 'r') as f:
        api = yaml.load(f, yaml.FullLoader)['api']['dongjak-gu']
    url = BASE_URL + api  \
        + f"?serviceKey={OPEN_API_KEY}&perPage=10&page=1"
    totalCount = requests.get(url).json()['totalCount']
    url = BASE_URL + api  \
        + f"?serviceKey={OPEN_API_KEY}&perPage={totalCount}"
    response = requests.get(url).json()['data']
    return response

@app.get("/seongbuk-gu")
async def seongdong_gu(request: Request):
    with open('api.yaml', 'r') as f:
        api = yaml.load(f, yaml.FullLoader)['api']['seongbuk-gu']
    url = BASE_URL + api  \
        + f"?serviceKey={OPEN_API_KEY}&perPage=10&page=1"
    totalCount = requests.get(url).json()['totalCount']
    url = BASE_URL + api  \
        + f"?serviceKey={OPEN_API_KEY}&perPage={totalCount}"
    response = requests.get(url).json()['data']
    return response

if __name__ =="__main__":
    pass