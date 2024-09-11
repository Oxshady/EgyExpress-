from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float, Integer
from models.Base import BaseModel
class Cart(BaseModel):
	"""Cart class"""
	description: Mapped['str'] = mapped_column(String(60), nullable=False)
	def __init__(self, *args, **kwargs) -> None:
		""" Initialize a new Cart object """
		super().__init__(*args, **kwargs)
