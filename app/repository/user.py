from sqlalchemy.orm import Session
import app.models as models, app.schema as schemas
from fastapi import HTTPException, status
from app.utils.hashing import Hash


def create(request: schemas.User, db: Session):
    new_user = models.User(
        first_name=request.first_name,
        middle_name=request.middle_name,
        last_name=request.last_name, 
        email=request.email, 
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all(db: Session):
    users = db.query(models.User).all()
    return users

def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user

def findByEmail(email: str, db: Session):
    user = db.query(models.User).filter(models.User.email == email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"User with the email {email} is not available")

    return user
