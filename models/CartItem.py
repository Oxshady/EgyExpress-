from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float, Integer
from models.Base import BaseModel

class CartItem(BaseModel):
    """CartItem class"""
    price: Mapped['float'] = mapped_column(Float, nullable=False)
    quantity: Mapped['int'] = mapped_column(Integer, nullable=False)
    product_id: Mapped['str'] = mapped_column(String(60), nullable=False)
    cart_id: Mapped['str'] = mapped_column(String(60), nullable=False)
    def __init__(self, *args, **kwargs) -> None:
        """ Initialize a new CartItem object """
        super().__init__(*args, **kwargs)
