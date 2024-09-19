from api.v1.views import api_v1
from flask import jsonify, request
from models import storage
from models.Review import Review
from flask_jwt_extended import jwt_required, get_jwt_identity
@api_v1.route('/reviews', methods=['GET', 'POST'])
@jwt_required()
def reviews():
    """ reviews endpoint """
    if request.method == 'GET':
        reviews = storage.get_all("Review")
        if reviews is None:
            return jsonify([])
        return jsonify([review.to_dict() for review in reviews])
    elif request.method == 'POST':
        user_id = get_jwt_identity()
        data = request.get_json()
        if data is None:
            return jsonify({"error": "Not a JSON"}), 400
        user = storage.get("User", user_id)
        rate = data.get('rate')
        description = data.get('description')
        product_id = data.get('product_id')
        product = storage.get("Product", product_id)
        if product is None:
            return jsonify({"error": "Product not found"}), 400
        review = Review(rate=rate, description=description, user=user, product=product)
        review.save()
        return jsonify({"success":True}), 201