from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.database import Base as Base
from sqlalchemy.orm import relationship


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="role_id")     
        
        