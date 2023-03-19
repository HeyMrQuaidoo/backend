from typing import List
from fastapi import APIRouter, Depends, status
import app.db.database as database, app.schema as schemas, app.utils as oauth2
from sqlalchemy.orm import Session
from app.repository import role

router = APIRouter(
    prefix="/role",
    tags=['Roles']
)

get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowRole])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return role.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.Role, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return role.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return role.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Role, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return role.update(id, request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowRole)
def show(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return role.show(id, db)
