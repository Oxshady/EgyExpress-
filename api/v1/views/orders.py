from api.v1.views import api_v1
from flask import jsonify, request
from models import storage
from models.Order import Order
from models.order_item import OrderItem
from models.Payment import Payment
from models.tracking import Tracking
from flask_jwt_extended import jwt_required, get_jwt_identity
@api_v1.route('/orders', methods=['GET', 'POST'])
@jwt_required()
def get_orders():
    """ Get all orders """
    if request.method == 'GET':
        orders = storage.get_all("Order")
        if orders is None:
            return jsonify([])
        return jsonify([order.to_dict() for order in orders])
    elif request.method == 'POST':
        user_id = get_jwt_identity()
        user = storage.get("User", user_id)
        if user is None:
            return jsonify({"error": "User not found"}), 404
        if user.cart is None or len(user.cart.cart_item) == 0:
            return jsonify({"error": "Cart is empty"})
        cart = user.cart
        cart_id = cart.id
        total_price = 0
        order_data = []
        for item in cart.cart_item:
            order_data.append({"product":item.product, "quantity": item.quantity, "price": item.price})
            total_price += item.price
        payment = Payment(payment_type="cash", user=user)
        payment.save()
        order = Order(total_price=total_price, user=user, payment=payment)
        order.save()
        for item in order_data:
            order_item = OrderItem(quantity=item.get('quantity'), price=item.get('price'), order=order, product=item.get('product'))
            order_item.save()
        tracking = Tracking(status="delivered", delivery_address="cairo", user=user, order=order)
        tracking.save()
        for item in cart.cart_item:
            item.delete()
        return jsonify({"success":True}), 201
