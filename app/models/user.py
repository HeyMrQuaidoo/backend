from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.database import Base as Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)

    role_id = relationship('Role', back_populates="user")
