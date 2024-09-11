from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from models.Base import BaseModel

class Traking(BaseModel):
    """Tracking class"""
    delivery_address: Mapped['str'] = mapped_column(String(100), nullable=False)
    status: Mapped['str'] = mapped_column(String(60), nullable=False)
    order_id: Mapped['str'] = mapped_column(String(60), nullable=False)
    
    def __init__(self, *args, **kwargs) -> None:
        """ Initialize a new Tracking object """
        super().__init__(*args, **kwargs)
