from api.v1.views import api_v1
from flask import jsonify
from models import storage

@api_v1.route('/users', methods=['GET'])
def get_users():
    """ Get all users """
    users = storage.get_all("User")
    if users is None:
        return jsonify([])
    return jsonify([user.to_dict() for user in users])

@api_v1.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
	""" Get a user """
	user = storage.get("User", user_id)
	if user is None:
		return jsonify({"error": "Not found"}), 404
	return jsonify(user.to_dict())
