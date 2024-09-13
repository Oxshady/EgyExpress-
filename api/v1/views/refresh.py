from flask import jsonify
from api.v1.views import api_v1
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

@api_v1.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    user_id = get_jwt_identity()
    access_token = create_access_token(identity=user_id)
    return jsonify(access_token=access_token), 200