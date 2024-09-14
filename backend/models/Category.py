from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from models.base import BaseModel, base
from typing import List
class Category(BaseModel, base):
    __tablename__ = 'categories'
    """Category class"""
    name: Mapped['str'] = mapped_column(String(60), nullable=False)
    description: Mapped['str'] = mapped_column(String(100), nullable=False)
    from models.Product import Product
    product: Mapped[List['Product']] = relationship(Product, backref='category', cascade='all, delete-orphan')
    from models.subCategory import Subcategory
    subcategory: Mapped[List['Subcategory']] = relationship(Subcategory, backref='category', cascade='all, delete-orphan')
    def __init__(self, *args, **kwargs) -> None:
        """ Initialize a new Category object """
        super().__init__(*args, **kwargs)
