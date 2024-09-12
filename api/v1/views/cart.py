from api.v1.views import api_v1
from flask import jsonify, request
from models import storage
from models.CartItem import CartItem
from models.Cart import Cart
@api_v1.route('/cart', methods=['GET', 'POST'])
def get_Cart():
    """ Get Cart """
    if request.method == 'GET':
        data = request.get_json()
        user_id = data.get('user_id')
        if user_id is None:
            return jsonify([])
        cart = storage.__session.query(Cart).filter_by(user_id=user_id).first()
        if cart is None:
            return jsonify([])
        for item in cart.cart_items:
            product_id = item.product_id
            price = item.price
            quantity = item.quantity
            product = storage.get("Product", product_id)
            product_data = {
            "product_name": product.name,
            "product_description": product.description,   
            "product_image" : product.image
            }
            return jsonify({"product": product_data, "quantity": quantity, "price": price})
    elif request.method == 'POST':
        if not request.is_json:
            return jsonify({"error": "Not a JSON"}), 400
        data = request.get_json()
        user_id = data.get('user_id')
        cart = storage.__session.query(Cart).filter_by(user_id=user_id).first()
        cart_items = data.get('cart_items')
        if cart_items is None:
            return jsonify({"error": "Missing cart_items"}), 400
        for item in cart_items:
            if item.get('product_id') is None:
                return jsonify({"error": "Missing product_id"}), 400
            if item.get('quantity') is None:
                return jsonify({"error": "Missing quantity"}), 400
            if item.get('price') is None:
                return jsonify({"error": "Missing price"}), 400
            product = storage.get("Product", item.get('product_id'))
            if product is None:
                return jsonify({"error": "Product not found"}), 404
            cart_item = CartItem(quantity=item.get('quantity'), price=item.get('price'), cart=cart, product=product)
            storage.post(cart_item)
        return None
