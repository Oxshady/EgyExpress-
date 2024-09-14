from sqlalchemy.orm import Mapped, relationship,mapped_column, backref
from sqlalchemy import String, ForeignKey
from models.base import BaseModel, base

class Payment(BaseModel, base):
    """Payment class"""
    __tablename__ = 'payment'
    payment_type: Mapped['str'] = mapped_column(String(60), nullable=False)
    user_id: Mapped['str'] = mapped_column(String(60), ForeignKey('users.id'), nullable=False)
    from models.Order import Order
    order: Mapped['Order'] = relationship(Order, uselist=False, backref=backref('payment', uselist=False))
    def __init__(self, *args, **kwargs) -> None:
        """ Initialize a new Payment object """
        super().__init__(*args, **kwargs)
