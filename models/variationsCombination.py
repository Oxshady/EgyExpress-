from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float
from models.Base import BaseModel

class VaiationCombination(BaseModel):
    """VaiationCombination class"""
    key_id: Mapped['str'] = mapped_column(String(60), nullable=False)
    value_id: Mapped['str'] = mapped_column(String(60), nullable=False)
    product_id: Mapped['str'] = mapped_column(String(60), nullable=False)
    def __init__(self, *args, **kwargs) -> None:
        """ Initialize a new VaiationCombination object """
        super().__init__(*args, **kwargs)