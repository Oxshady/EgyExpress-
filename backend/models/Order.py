from sqlalchemy.orm import Mapped, mapped_column, backref, relationship
from sqlalchemy import String, Float, ForeignKey
from models.base import BaseModel, base
from typing import List
class Order(BaseModel, base):
	"""Order class"""
	__tablename__ = 'orders'
	total_price: Mapped['float'] = mapped_column(Float, nullable=False)
	user_id: Mapped['str'] = mapped_column(String(60), ForeignKey('users.id') , nullable=False)
	payment_id: Mapped['str'] = mapped_column(String(60), ForeignKey('payment.id') , nullable=False)
	from models.tracking import Tracking
	tracking: Mapped['Tracking'] = relationship(Tracking, uselist=False,backref=backref('order', uselist=False))
	from models.order_item import OrderItem
	order_item: Mapped[List['OrderItem']] = relationship(OrderItem, backref='order', cascade='all, delete-orphan')
	def __init__(self, *args, **kwargs) -> None:
		""" Initialize a new Order object """
		super().__init__(*args, **kwargs)
