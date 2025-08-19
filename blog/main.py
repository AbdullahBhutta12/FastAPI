import uvicorn
from fastapi import FastAPI
from schemas import *

app = FastAPI()


@app.post('/blog')
def create(request: Blog):
    return request

