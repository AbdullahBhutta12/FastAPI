# import uvicorn
from fastapi import FastAPI, Depends, status, Response, HTTPException
from blog import models
from blog.database import engine, SessionLocal
from blog import schemas
from sqlalchemy.orm import Session

models.Base.metadata.create_all(engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.boby)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(id == models.Blog.id).\
        update({models.Blog.title:models.Blog.title - request}, synchronize_session=False)
    db.query(models.Blog).filter(id == models.Blog.id).\
        update({"title": models.Blog.title - request}, synchronize_session="evaluate")
    db.commit()
    return 'updated'


@app.get('/blog')
def all(db: Session = Depends(get_db)):
    blog = db.query(models.Blog).all()
    return blog


@app.get('/blog/{id}', status_code=200)
def show(id: int, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(id == models.Blog.id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not available")
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {'detail': f"Blog with id {id} is not available"}
    return blog


@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(id == models.Blog.id).delete(synchronize_session=False)
    db.commit()
    return 'done'

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=9000, reload=True)
