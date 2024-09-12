from api.v1.views import api_v1
from flask import jsonify
from models import storage
from models.users import User

@api_v1.route('/users', methods=['GET'])
def get_users():
    """ Get all users """
    return jsonify([user.to_dict() for user in storage.get_all("User")])
