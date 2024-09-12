from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float, Integer, ForeignKey
from models.base import BaseModel, base

class CartItem(BaseModel, base):
    """CartItem class"""
    __tablename__ = 'cart_item'
    price: Mapped['float'] = mapped_column(Float, nullable=False)
    quantity: Mapped['int'] = mapped_column(Integer, nullable=False)
    product_id: Mapped['str'] = mapped_column(String(60), ForeignKey('products.id'),nullable=False)
    cart_id: Mapped['str'] = mapped_column(String(60), ForeignKey('cart.id'),nullable=False)
    def __init__(self, *args, **kwargs) -> None:
        """ Initialize a new CartItem object """
        super().__init__(*args, **kwargs)
