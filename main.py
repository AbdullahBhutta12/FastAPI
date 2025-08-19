# import uvicorn
from fastapi import FastAPI, Query
from typing import Optional, Annotated
from pydantic import BaseModel


app = FastAPI()


@app.get('/blog')
def index(limit: int, published: bool = True, sort: Annotated[str | None, Query(max_length=50)] = None):

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
def show(id, limit=20):
    return {'data': {'1', '2'} }


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f"Blog is created with title as {blog.title}"}

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)