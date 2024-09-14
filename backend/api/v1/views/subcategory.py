from api.v1.views import api_v1
from flask import jsonify, request
from models import storage
@api_v1.route('/subcategories', methods=['GET'])
def get_subcategories():
    return jsonify([subcategory.to_dict() for subcategory in storage.get_all("Subcategory")])

@api_v1.route('/subcategories/products', methods=['GET', 'POST'])
def get_subcategory_products():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Not a JSON"}), 400
    subcategory_id = data.get('subcategory_id')
    if subcategory_id is None:
        return jsonify({"error": "Missing category_id"}), 400
    products = [product.to_dict() for product in storage.get("Subcategory", subcategory_id).product]
    return jsonify(products), 200
