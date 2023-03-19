from typing import List, Optional
from pydantic import BaseModel

class RoleBase(BaseModel):
    title: str
    body: str

class User(BaseModel):
    first_name:str
    middle_name:str
    last_name:str
    email:str
    password:str

class Role(RoleBase):
    class Config():
        orm_mode = True
        
class ShowUser(BaseModel):
    first_name:str
    middle_name:str
    last_name:str
    email:str
    roles : List[Role] =[]
    class Config():
        orm_mode = True

class Login(BaseModel):
    email: str
    password:str