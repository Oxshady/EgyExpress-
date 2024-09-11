from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer,String, Float
from models.Base import BaseModel

class Product(BaseModel):
	"""Product class"""
	name: Mapped['str'] = mapped_column(String(60), nullable=False)
	description: Mapped['str'] = mapped_column(String(100), nullable=False)
	quantity: Mapped['int'] = mapped_column(Integer, nullable=False)
	price: Mapped['float'] = mapped_column(Float, nullable=False)
	category_id: Mapped['str'] = mapped_column(String(60), nullable=False)
	subcategory_id: Mapped['str'] = mapped_column(String(60), nullable=False)
	
	def __init__(self, *args, **kwargs) -> None:
		""" Initialize a new Product object """
		super().__init__(*args, **kwargs)
