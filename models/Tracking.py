from sqlalchemy.orm import relationship,Mapped, mapped_column
from sqlalchemy import String, ForeignKey
from models.base import BaseModel, base

class Tracking(BaseModel, base):
    """Tracking class"""
    __tablename__ = 'tracking'
    delivery_address: Mapped['str'] = mapped_column(String(100), nullable=False)
    status: Mapped['str'] = mapped_column(String(60), nullable=False)
    order_id: Mapped['str'] = mapped_column(String(60), nullable=False)
    user_id: Mapped['str'] = mapped_column(String(60), ForeignKey('users.id'),nullable=False)
    def __init__(self, *args, **kwargs) -> None:
        """ Initialize a new Tracking object """
        super().__init__(*args, **kwargs)
