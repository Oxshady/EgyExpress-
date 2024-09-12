from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String, Float, ForeignKey, Integer
from models.base import BaseModel, base

class OrderItem(BaseModel, base):
    __tablename__ = 'order_item'
    price: Mapped['float'] = mapped_column(Float, nullable=False)
    quantity: Mapped['int'] = mapped_column(Integer, nullable=False)
    order_id: Mapped['str'] = mapped_column(String(60), ForeignKey('orders.id'),nullable=False)
    product_id: Mapped['str'] = mapped_column(String(60), ForeignKey('products.id'),nullable=False)
    def __init(self, *args, **kwargs) -> None:
        """ Initialize a new OrderItem object """
        super().__init__(*args, **kwargs)