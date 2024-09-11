from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float
from models.Base import BaseModel

class OrderItem(BaseModel):
    price: Mapped['float'] = mapped_column(Float, nullable=False)
    order_id: Mapped['str'] = mapped_column(String(60), nullable=False)
    product_id: Mapped['str'] = mapped_column(String(60), nullable=False)
    def __init(self, *args, **kwargs) -> None:
        """ Initialize a new OrderItem object """
        super().__init__(*args, **kwargs)