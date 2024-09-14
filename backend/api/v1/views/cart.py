from api.v1.views import api_v1
from flask import jsonify, request
from models import storage
from models.CartItem import CartItem
from models.Cart import Cart
from flask_jwt_extended import jwt_required, get_jwt_identity
@api_v1.route('/cart', methods=['GET', 'POST'])
@jwt_required()
def get_Cart():
    """ Get Cart """
    if request.method == 'GET':
        from models.users import User
        user_id = get_jwt_identity()
        user = storage.get("User", user_id)
        cart = storage.filter_one("Cart", user_id=user_id)
        if cart is None:
            return jsonify({"error": "Cart not found"}), 404
        if len(cart.cart_item) == 0:
            return jsonify({"error": "Cart is empty"})
        for item in cart.cart_item:
            product_id = item.product_id
            price = item.price
            quantity = item.quantity
            product = storage.get("Product", product_id)
            product_data = {
            "product_name": product.name,
            "product_description": product.description
            }
            return jsonify({"product": product_data, "quantity": quantity, "price": price})
    elif request.method == 'POST':
        if not request.is_json:
            return jsonify({"error": "Not a JSON"}), 400
        data = request.get_json()
        if data is None:
            return jsonify({"error": "Not a JSON"}), 400
        user_id = get_jwt_identity()
        cart = storage.filter_one("Cart", user_id=user_id)
        product_id = data.get('product_id')
        if product_id is None:
            return jsonify({"error": "Missing product_id"}), 400
        quantity = data.get('quantity')
        if quantity is None:
            return jsonify({"error": "Missing quantity"}), 400
        price = data.get('price')
        if price is None:
            return jsonify({"error": "Missing price"}), 400
        product = storage.get("Product", product_id)
        if product is None:
            return jsonify({"error": "Product not found"}), 404
        cart_item = CartItem(quantity=quantity, price=price, cart=cart, product=product)
        cart_item.save()
        return jsonify({"success":True}), 201
