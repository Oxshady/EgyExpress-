from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float
from models.Base import BaseModel

class Order(BaseModel):
	"""Order class"""
	total_price: Mapped['str'] = mapped_column(String(60), nullable=False)
	tracking_id: Mapped['str'] = mapped_column(String(60), nullable=False)
	user_id: Mapped['str'] = mapped_column(String(60), nullable=False)
	payment_id: Mapped['str'] = mapped_column(String(60), nullable=False)
	def __init__(self, *args, **kwargs) -> None:
		""" Initialize a new Order object """
		super().__init__(*args, **kwargs)
