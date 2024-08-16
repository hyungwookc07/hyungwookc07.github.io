from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse


app = FastAPI()
templates = Jinja2Templates(directory="static")

app.mount("/static", StaticFiles(directory="static", html=True), name="index")