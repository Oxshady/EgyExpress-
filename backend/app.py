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
user = User(first_name="shadi", last_name="shadi", phoneNumber="123456789", address="cairo", email="shadi@hotmail.com",password="123456")
user.save()

cart = Cart(description="asdsadsads",user=user)
cart.save()

payment = Payment(payment_type="visa",user=user)
payment.save()

order = Order(total_price=200,user=user, payment=payment)
order.save()

category = Category(name="sadasd", description="sadads")
category.save()

sub = Subcategory(name="sadasd", description="sadasd", category=category)
sub.save()


discount = Discount(rate="20")
discount.save()

key = VaiationKey(key="sadasd")
key.save()
value = VaiationValue(value="sadasd")
value.save()
variation = VaiationCombination(key=key, value=value)
variation.save()

product = Product(name="sadasd", price=200, description="sadasd", category=category,subcategory=sub, quantity=2, discount=discount, variation_combination=[variation])
product.save()
cart_item = CartItem(quantity=2, price=200,cart=cart, product=product)
cart_item.save()

orderItem = OrderItem(quantity=2, order=order, price=200, product=product)
orderItem.save()

tracking = Tracking(status="delivered",delivery_address="sadasd",user=user, order=order)
tracking.save()

r = Review(rate=5, description="good", product=product,user=user)
r.save()
