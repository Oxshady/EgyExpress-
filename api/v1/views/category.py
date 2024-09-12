from api.v1.views import api_v1
from flask import jsonify, request
from models import storage
@api_v1.route('/categories', methods=['GET'])
def get_categories():
    return jsonify([category.to_dict() for category in storage.get_all("Category")])

@api_v1.route('/categories/products', methods=['GET', 'POST'])
def get_category_products():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Not a JSON"}), 400
    category_id = data.get('category_id')
    if category_id is None:
        return jsonify({"error": "Missing category_id"}), 400
    products = [product.to_dict() for product in storage.get("Category", category_id).product]
    return jsonify(products), 200
