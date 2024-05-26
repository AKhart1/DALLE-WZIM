import json
import os
import requests
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="Dall-E WZIM",
    version="1.0.0"
)

templates = Jinja2Templates(directory="app/templates")

@app.get("/get-image", response_class=HTMLResponse)
def index(request: Request):
    api_key = os.getenv("MY_SECRET")
    
    url = 'https://api.openai.com/v1/images/generations'

    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
    }

    data = {
    'prompt': "Italy Sunset",
    'model': "dalle-e-3",
    'n': 1,  # Number of images to generate
    'size': '1024x1024'  # Desired size of the generated image 
    }

    print(f'The secret is: {api_key}')

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_data = response.json()
        return templates.TemplateResponse("index.html", {"request": request, "response": response_data['data'][0]['url']})
    else:
        return templates.TemplateResponse("index.html", {"request": request, "response": "Image wasn't generated"})