from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer
from models.base import BaseModel, base
from typing import List
class Discount(BaseModel, base):
	"""Discount class"""
	__tablename__ = 'discount'
	rate: Mapped['int'] = mapped_column(Integer, nullable=False)
	from models.Product import Product
	product: Mapped[List['Product']] = relationship(Product, backref='discount', cascade='all, delete-orphan')
	def __init__(self, *args, **kwargs) -> None:
		""" Initialize a new Discount object """
		super().__init__(*args, **kwargs)
