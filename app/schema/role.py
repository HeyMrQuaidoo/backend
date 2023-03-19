from typing import List, Optional
from pydantic import BaseModel
from .user import ShowUser

class RoleBase(BaseModel):
    name: str
    description: str

class Role(RoleBase):
    class Config():
        orm_mode = True

class ShowRole(BaseModel):
    name: str
    description: str
    user: ShowUser

    class Config():
        orm_mode = True