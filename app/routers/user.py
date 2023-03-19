from fastapi import APIRouter
from typing import List
import app.db.database as database, app.schema as schemas, app.models as models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from app.repository import user as user_service
from app.utils.jwt.auth_handler import signJWT
from app.utils.jwt.auth_bearer import JWTBearer
from app.utils.hashing import Hash

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user_service.create(request, db)

@router.get('/', response_model=List[schemas.ShowUser])
def get_user(db: Session = Depends(get_db)):
    return user_service.get_all(db)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user_service.show(id, db)

@router.post("/protected", dependencies=[Depends(JWTBearer())])
def add_post(request: schemas.User, db: Session = Depends(get_db)):
    return {
        "data": "Protected route"
    }