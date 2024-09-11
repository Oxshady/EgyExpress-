from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from models.Base import BaseModel

class Category(BaseModel):
    """Category class"""
    name: Mapped['str'] = mapped_column(String(60), nullable=False)
    description: Mapped['str'] = mapped_column(String(100), nullable=False)
    
    def __init__(self, *args, **kwargs) -> None:
        """ Initialize a new Category object """
        super().__init__(*args, **kwargs)
