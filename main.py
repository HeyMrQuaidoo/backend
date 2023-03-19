import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import app.models as models
from app.db import engine
from app.routers import user, role, auth

app = FastAPI()
origins = ["*"]  

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
models.Base.metadata.create_all(engine)

app.include_router(user.router)
app.include_router(role.router)
app.include_router(auth.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)