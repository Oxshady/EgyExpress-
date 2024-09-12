from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float, ForeignKey
from models.base import BaseModel, base



class VaiationCombination(BaseModel, base):
    """VaiationCombination"""
    __tablename__ = 'VaiationCombination'
    key_id: Mapped['str'] = mapped_column(String(60), ForeignKey('VaiationKey.id'),nullable=False)
    value_id: Mapped['str'] = mapped_column(String(60), ForeignKey('VaiationValue.id'),nullable=False)
    def __init__(self, *args, **kwargs) -> None:
        """ Initialize a new VaiationCombination object """
        super().__init__(*args, **kwargs)
