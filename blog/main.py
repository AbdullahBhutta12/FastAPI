# import uvicorn
from fastapi import FastAPI, Depends
from blog import models
from blog.database import engine, SessionLocal
from blog.schemas import Blog
from sqlalchemy.orm import Session

models.Base.metadata.create_all(engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog')
def create(request: Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.boby)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blog')
def all(db: Session = Depends(get_db)):
    blog = db.query(models.Blog).all()
    return blog


@app.get('/blog/{id}')
def show(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(id == models.Blog.id).first()
    return blog

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=9000, reload=True)
