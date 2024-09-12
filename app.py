from models.base import base
from models.tracking import Tracking
from models.Category import Category
from models.subCategory import Subcategory
from models.Discount import Discount
from models.Comb import VaiationCombination
from models.variationsKey import VaiationKey
from models.variationsValue import VaiationValue
from models.Product import Product
from models.order_item import OrderItem
from models.Order import Order
from models.Payment import Payment
from models.CartItem import CartItem
from models.Cart import Cart
from models.Review import Review

from models.users import User
from models.storage.db import DBstorage

d = DBstorage()
d.setup()
session = d.get_session()
user = User(first_name="shadi", last_name="shadi", phoneNumber="123456789", address="cairo", email="shadi@hotmail.com",password="123456")
session.add(user)
session.commit()

cart = Cart(description="asdsadsads",user=user)
session.add(cart)
session.commit()

payment = Payment(payment_type="visa",user=user)
session.add(payment)
session.commit()

order = Order(total_price="200",user=user, payment=payment)
session.add(order)
session.commit()

category = Category(name="sadasd", description="sadads")
session.add(category)
session.commit()

sub = Subcategory(name="sadasd", description="sadasd", category=category)
session.add(sub)
session.commit()


discount = Discount(rate="20")
session.add(discount)
session.commit()
key = VaiationKey(key="sadasd")
session.add(key)
session.commit()
value = VaiationValue(value="sadasd")
session.add(value)
session.commit()
variation = VaiationCombination(key=key, value=value)
session.add(variation)
session.commit()

product = Product(name="sadasd", price=200, description="sadasd", category=category,subcategory=sub, quantity=2, discount=discount, variation_combination=[variation])
session.add(product)
session.commit()

cart_item = CartItem(quantity=2, price=200,cart=cart, product=product)
session.add(cart_item)
session.commit()

orderItem = OrderItem(quantity=2, order=order, price=200, product=product)
session.add(orderItem)
session.commit()

tracking = Tracking(status="delivered",delivery_address="sadasd",user=user, order=order)
session.add(tracking)
session.commit()

r = Review(rate=5, description="good", product=product,user=user)
session.add(r)
session.commit()