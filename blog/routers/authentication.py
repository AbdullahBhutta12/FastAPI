from fastapi import APIRouter, Depends, status, HTTPException
from blog import schemas, models
from sqlalchemy.orm import Session
from blog.database import *

router = APIRouter(
    tags=['authentication']
)


@router.get('/login')
def login(request: schemas.login, db: Session = Depends(get_db())):
    user = db.query(models.User).filter(request.username == models.User.email)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    return user
