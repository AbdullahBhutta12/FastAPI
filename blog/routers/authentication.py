from fastapi import APIRouter, Depends, status, HTTPException
from blog import schemas, models
from sqlalchemy.orm import Session
from blog.database import *
from blog.hashing import Hash
router = APIRouter(
    tags=['authentication']
)


@router.post('/login')
def login(request: schemas.login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(request.username == models.User.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Invalid Credentials")
    if Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Incorrect password")
    return user