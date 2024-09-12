from sqlalchemy.orm import Mapped, mapped_column, relationship, backref
from sqlalchemy import String, ForeignKey, Integer
from models.base import BaseModel,base
from typing import List
class Cart(BaseModel, base):
	"""Cart class"""
	__tablename__ = 'cart'
	description: Mapped['str'] = mapped_column(String(60), nullable=False)
	user_id: Mapped['str'] = mapped_column(String(60), ForeignKey('users.id'), nullable=False)
	from models.CartItem import CartItem
	cart_item: Mapped[List['CartItem']] = relationship(CartItem, backref='cart', cascade='all, delete-orphan')
	def __init__(self, *args, **kwargs) -> None:
		""" Initialize a new Cart object """
		super().__init__(*args, **kwargs)
