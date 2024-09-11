from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float
from models.Base import BaseModel

class VaiationKey(BaseModel):
    """VaiationCombination class"""
    value: Mapped['str'] = mapped_column(String(60), nullable=False)
    def __init__(self, *args, **kwargs) -> None:
        """ Initialize a new VaiationValue object """
        super().__init__(*args, **kwargs)