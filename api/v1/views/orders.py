from api.v1.views import api_v1
from flask import jsonify
from models import storage
from models.Order import Order

@api_v1.route('/orders', methods=['GET'])
def get_orders():
    """ Get all orders """
    return jsonify([order.to_dict() for order in storage.get_all("Order")])
