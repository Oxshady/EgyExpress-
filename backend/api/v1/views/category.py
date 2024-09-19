from api.v1.views import api_v1
from flask import jsonify, request
from models import storage

@api_v1.route('/categories', methods=['GET'])
def get_categories():
    categories = storage.get_all("Category")
    try:
        if categories is None:
            return jsonify([]), 400
        return jsonify([category.to_dict() for category in categories]), 200
    except Exception as e:
        storage.roll()
        return jsonify([]), 400


@api_v1.route('/products/categories/<category_id>', methods=['GET'])
def get_category_products(category_id):
    try:
        cid = category_id
        if cid is None:
            print("Category ID is None")
            print(cid)
            return jsonify([]), 400
        products = [p.to_dict() for p in storage.get("Category", cid).product]
        if products is None:
            return jsonify([]), 400
        return jsonify(products), 200
    except Exception as e:
        storage.roll()
        return jsonify([]), 400
