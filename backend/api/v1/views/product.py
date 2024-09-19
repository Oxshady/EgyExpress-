#!/usr/bin/python3
""" shows user info on the profile page and allow for editing these info and logout and delete user acc """
from models import storage
from api.v1.views import api_v1
from flask import jsonify, request

@api_v1.route('/product/<product_id>', methods=['GET'])
def get_product(product_id):
	""" Get Product """
	if request.method == 'GET':
		product = storage.get("Product", product_id)
		if product is None:
			return jsonify([])
		return jsonify(product.to_dict()), 200
