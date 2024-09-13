from api.v1.views import api_v1
from flask import jsonify, request
from models import storage
from models.Order import Order
from models.order_item import OrderItem
from models.Payment import Payment
from models.tracking import Tracking
@api_v1.route('/orders', methods=['GET', 'POST'])
def get_orders():
    """ Get all orders """
    if request.method == 'GET':
        orders = storage.get_all("Order")
        if orders is None:
            return jsonify([])
        return jsonify([order.to_dict() for order in orders])
    elif request.method == 'POST':
        user = storage.get_all("User")[0]
        return_data = "hi"
        cart = user.cart
        cart_id = cart.id
        total_price = 0
        order_data = []
        for item in cart.cart_item:
            order_data.append({"product":item.product, "quantity": item.quantity, "price": item.price})
            total_price += item.price
        payment = Payment(payment_type="cash", user=user)
        storage.post(payment)
        order = Order(total_price=total_price, user=user, payment=payment)
        storage.post(order)
        for item in order_data:
            order_item = OrderItem(quantity=item.get('quantity'), price=item.get('price'), order=order, product=item.get('product'))
            storage.post(order_item)
        tracking = Tracking(status="delivered", delivery_address="cairo", user=user, order=order)
        storage.post(tracking)
        for item in cart.cart_item:
            storage.delete(item)
        return jsonify(return_data)