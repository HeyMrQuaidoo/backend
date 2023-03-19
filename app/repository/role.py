from sqlalchemy.orm import Session
import app.models as models
import app.schema as schemas
from fastapi import HTTPException, status


def get_all(db: Session):
    roles = db.query(models.Role).all()
    return roles


def create(request: schemas.Role, db: Session):
    new_role = models.Role(name=request.name, body=request.description, user_id=1)
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role


def destroy(id: int, db: Session):
    role = db.query(models.Role).filter(models.Role.id == id)

    if not role.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Role with id {id} not found")

    role.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(id: int, request: schemas.Role, db: Session):
    role = db.query(models.Role).filter(models.Role.id == id)

    if not role.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Role with id {id} not found")

    role.update(request)
    db.commit()
    return 'updated'


def show(id: int, db: Session):
    role = db.query(models.Role).filter(models.Role.id == id).first()
    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Role with the id {id} is not available")
    return role
