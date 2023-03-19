from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import app.db.database as database, app.models as models, app.utils.token as token, app.schema as schemas
from app.repository import user as user_service

# Auth
from app.utils.jwt.auth_handler import signJWT
from app.utils.hashing import Hash

router = APIRouter(
    tags=['Authentication']
)

get_db = database.get_db

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(
        models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")

    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

def check_user(data: schemas.Login, db: Session = Depends(get_db)):
    current_user = user_service.findByEmail(data.email, db)
    
    if current_user.email == data.email and Hash.verify(current_user.password, data.password):
        return True
    return False

@router.post('/auth', response_model=schemas.Token)
def user_login(request: schemas.Login, db: Session = Depends(get_db)):
    if check_user(request, db):
        return signJWT(request.email)
    return {
        "error": "Wrong login details!"
    }