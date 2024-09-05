from pydantic import BaseModel, validator
from pydantic_core import PydanticCustomError
from sqlalchemy import Column, String, Integer, Boolean
from database.db import db
from typing import Optional
from api.utils.serializer import Serializer

class TaskDB(db.Model, Serializer):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(120), nullable=True)
    done = Column(Boolean, nullable=False)
    
    def __init__(self, name, description, done, id: Optional[int] = None):
        self.name = name
        self.description = description
        self.id = id
        self.done = done
        
    def serialize(self):
        d = Serializer.serialize(self)
        return d
    
class Task(BaseModel):
    name:str
    description:str
    id: int = None
    done: bool
    
    def __init__(self, name, description, done):
        super().__init__(name=name, description=description, done=done)

    def __repr__(self):
        return f"<Task {self.name}, {self.description}>"
    
    @validator('name')
    def validate_name(cls, value):
        if value == "":
            raise PydanticCustomError(
                'Name is empty',
                'Name value is empty", got "{wrong_value}"',
                dict(wrong_value=value),
            )
        elif len(value) < 4:
            raise PydanticCustomError(
                'Name length is less than 4 chars',
                'Name length is less than 4 chars", got "{wrong_value}"',
                dict(wrong_value=value),
            )
        return value
    
    @validator('description')
    def validate_desc(cls, value):
        if 1 <= len(value) <= 5:
            raise PydanticCustomError(
                'Description length is less than 6 chars',
                'Description length is less than 6 chars", got "{wrong_value}"',
                dict(wrong_value=value),
            )
        return value
    
    