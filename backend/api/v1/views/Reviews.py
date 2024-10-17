from api.v1.views import api_v1
from flask import jsonify, request
from models import storage
from models.Review import Review
from flask_jwt_extended import jwt_required, get_jwt_identity
@api_v1.route('/reviews', methods=['POST'], strict_slashes=False)
@jwt_required()
def add_review():
    """ reviews endpoint """
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
        return jsonify({"error": "Product not found"}), 401
    review = Review(rate=rate, description=description, user=user, product=product)
    review.save()
    return jsonify({"success":True}), 201

@api_v1.route('/reviews/get', methods=['GET'], strict_slashes=False)
def get_reviews():
    """ get reviews """
    product_id = request.args.get('product_id')
    if not product_id:
        return jsonify({"error": "Missing product_id"}), 400
    reviews = storage.filter_group("Review", product_id=product_id)
    if reviews is None:
        return jsonify([])
    reviews_list = []
    for review in reviews:
        user = storage.get("User", review.user_id)
        review_dict = {
            'rate': review.rate,
            'description': review.description,
            'user_name': f"{user.first_name} {user.last_name}" if user else "Unknown"
        }
        reviews_list.append(review_dict)
    return jsonify(reviews_list)
