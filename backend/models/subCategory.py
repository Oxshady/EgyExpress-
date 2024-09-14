from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from models.base import BaseModel, base
from typing import List
class Subcategory(BaseModel, base):
	"""Subcategory class"""
	__tablename__ = 'subcategories'
	name: Mapped['str'] = mapped_column(String(60), nullable=False)
	description: Mapped['str'] = mapped_column(String(100), nullable=False)
	category_id: Mapped['str'] = mapped_column(String(60), ForeignKey('categories.id'),nullable=False)
	from models.Product import Product
	product: Mapped[List['Product']] = relationship(Product, backref='subcategory', cascade='all, delete-orphan')
	def __init__(self, *args, **kwargs) -> None:
		""" Initialize a new Subcategory object """
		super().__init__(*args, **kwargs)
