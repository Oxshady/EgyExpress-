from sqlalchemy.orm import Mapped, relationship ,mapped_column
from sqlalchemy import String, Float
from models.base import BaseModel, base
from typing import List
class VaiationValue(BaseModel, base):
    """VaiationValue class"""
    __tablename__ = 'VaiationValue'
    value: Mapped['str'] = mapped_column(String(60), nullable=False)
    from models.Comb import VaiationCombination
    combination: Mapped[List['VaiationCombination']] = relationship(VaiationCombination, backref='value', cascade='all, delete-orphan')
    def __init__(self, *args, **kwargs) -> None:
        """ Initialize a new VaiationValue object """
        super().__init__(*args, **kwargs)