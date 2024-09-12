from sqlalchemy.orm import Mapped,relationship , mapped_column
from sqlalchemy import String, Float
from models.base import BaseModel, base
from typing import List
class VaiationKey(BaseModel, base):
    """VaiationKey class"""
    __tablename__ = 'VaiationKey'
    key: Mapped['str'] = mapped_column(String(60), nullable=False)
    from models.Comb import VaiationCombination
    combination: Mapped[List['VaiationCombination']] = relationship(VaiationCombination, backref='key', cascade='all, delete-orphan')
    def __init__(self, *args, **kwargs) -> None:
        """ Initialize a new VaiationKey object """
        super().__init__(*args, **kwargs)
