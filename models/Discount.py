from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from models.Base import BaseModel

class discount(BaseModel):
	"""Discount class"""
	rate: Mapped['int'] = mapped_column(Integer, nullable=False)
	product_id: Mapped['str'] = mapped_column(String(60), nullable=False)
	def __init__(self, *args, **kwargs) -> None:
		""" Initialize a new Discount object """
		super().__init__(*args, **kwargs)
