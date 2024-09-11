from sqlalchemy import String, DateTime
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from uuid import uuid4
from datetime import datetime
base = declarative_base()

class BaseModel:
    """ Base class for all models """
    id: Mapped['str'] = mapped_column(String(60), primary_key=True, default=lambda: uuid4().hex)
    created_at: Mapped['datetime'] = mapped_column(DateTime, default=datetime.utcnow())
    updated_at: Mapped['datetime'] = mapped_column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())
    
    def __init__(self, *args, **kwargs) -> None:
        """ Initialize a new Base object """
        for key, value in kwargs.items():
            setattr(self, key, value)
        if not self.id:
            self.id = uuid4().hex
        if not self.created_at:
            self.created_at = datetime.utcnow()
        if not self.updated_at:
            self.updated_at = datetime.utcnow()
    
    def to_dict(self):
        """ Return a dictionary representation of the object """
        return self.__dict__
    