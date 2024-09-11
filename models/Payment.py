from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float
from models.Base import BaseModel

class Payment(BaseModel):
    """Payment class"""
    payment_type: Mapped['str'] = mapped_column(String(60), nullable=False)
    order_id: Mapped['str'] = mapped_column(String(60), nullable=False)
    def __init__(self, *args, **kwargs) -> None:
        """ Initialize a new Payment object """
        super().__init__(*args, **kwargs)
