from sqlalchemy.orm import Mapped, relationship,mapped_column
from sqlalchemy import Integer,String, Float, ForeignKey, Table, Column
from models.base import BaseModel, base
from typing import List

product_variation_combination = Table(
    'product_variation_combination',
    base.metadata,
    Column('product_id', String(60), ForeignKey('products.id'), nullable=False),
    Column('variation_combination_id', String(60), ForeignKey('VaiationCombination.id'),nullable=False),
    )


class Product(BaseModel, base):
	"""Product class"""
	__tablename__ = 'products'
	name: Mapped['str'] = mapped_column(String(60), nullable=False)
	description: Mapped['str'] = mapped_column(String(100), nullable=False)
	quantity: Mapped['int'] = mapped_column(Integer, nullable=False)
	price: Mapped['float'] = mapped_column(Float, nullable=False)
	category_id: Mapped['str'] = mapped_column(String(60), ForeignKey('categories.id'),nullable=False)
	subcategory_id: Mapped['str'] = mapped_column(String(60), ForeignKey('subcategories.id'),nullable=False)
	discount_id: Mapped['str'] = mapped_column(String(60), ForeignKey('discount.id'),nullable=False)
	from models.order_item import OrderItem
	order_item: Mapped[List['OrderItem']] = relationship(OrderItem, backref='product', cascade='all, delete-orphan')
	from models.CartItem import CartItem
	cart_item: Mapped[List['CartItem']] = relationship(CartItem, backref='product', cascade='all, delete-orphan')
	from models.Review import Review
	review: Mapped[List['Review']] = relationship(Review, backref='product', cascade='all, delete-orphan')
	from models.Comb import VaiationCombination
	variation_combination: Mapped[List['VaiationCombination']] = relationship(VaiationCombination, secondary=product_variation_combination, backref='product', cascade='all, delete-orphan', single_parent=True)
	def __init__(self, *args, **kwargs) -> None:
		""" Initialize a new Product object """
		super().__init__(*args, **kwargs)
