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
user = User(first_name="shadi", last_name="mahmoud", phoneNumber="01020367515", address="cairo", email="shadi@hotmail.com",password="123456")
user.save()

cart = Cart(description=f"user {user.first_name}",user=user)
cart.save()

payment = Payment(payment_type="visa",user=user)
payment.save()

order = Order(total_price=200,user=user, payment=payment)
order.save()

category = Category(name="electronics", description="electronics devices")
category.save()

sub = Subcategory(name="mobiles", description="mobiles devices", category=category)
sub.save()


discount = Discount(rate="20")
discount.save()

key = VaiationKey(key="color")
key.save()
value = VaiationValue(value="black")
value.save()
variation = VaiationCombination(key=key, value=value)
variation.save()
key = VaiationKey(key="size")
key.save()
value = VaiationValue(value="large")
value.save()
variation = VaiationCombination(key=key, value=value)
variation.save()

product = Product(image="https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg",name="iphone 10", price=200, description="iphone 10 device", category=category,subcategory=sub, quantity=2, discount=discount, variation_combination=[variation])
product.save()
cart_item = CartItem(quantity=2, price=200,cart=cart, product=product)
cart_item.save()

orderItem = OrderItem(quantity=2, order=order, price=200, product=product)
orderItem.save()

tracking = Tracking(status="delivered",delivery_address="gize, 6 october",user=user, order=order)
tracking.save()

r = Review(rate=5, description="good", product=product,user=user)
r.save()
