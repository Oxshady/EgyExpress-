from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float
from models.Base import BaseModel

class VaiationKey(BaseModel):
    """VaiationCombination class"""
    key: Mapped['str'] = mapped_column(String(60), nullable=False)
    def __init__(self, *args, **kwargs) -> None:
        """ Initialize a new VaiationKey object """
        super().__init__(*args, **kwargs)
