from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, ForeignKey
from models.base import BaseModel, base

class Review(BaseModel, base):
    """Review class"""
    __tablename__ = 'reviews'
    rate: Mapped['int'] = mapped_column(Integer, nullable=False)
    description: Mapped['str'] = mapped_column(String(100), nullable=False)
    product_id: Mapped['str'] = mapped_column(String(60), ForeignKey('products.id'),nullable=False)
    user_id: Mapped['str'] = mapped_column(String(60), ForeignKey('users.id'),nullable=False)
    def __init__(self, *args, **kwargs) -> None:
        """ Initialize a new Review object """
        super().__init__(*args, **kwargs)
