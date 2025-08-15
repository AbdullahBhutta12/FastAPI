import uvicorn
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]



@app.get('/blog')
def index(limit: int, published: bool = True, sort: Optional[str] = None):

    if published:
        return {'data': f'{limit} published blogs from db'}
    else:
        return {'data': f'{limit} blog from db'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs' }


@app.get('/blog/{id}')
def show(id: int):
    return {'data': id }

@app.get('/blog/{id}/comments')
def show(id: int):
    return { 'data': id }

@app.post('/blog')
def create_blog(request: Blog):

    return {'data': f"Blog is created with title as {request.title}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

