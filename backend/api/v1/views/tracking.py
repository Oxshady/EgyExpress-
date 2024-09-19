#!/usr/bin/python3
""" shows user info on the profile page and allow for editing these info and logout and delete user acc """
from models import storage
from api.v1.views import api_v1
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
@api_v1.route('/tracking', methods=['GET'])
@jwt_required()
def tracking():
    if request.method == 'GET':
        user_id = get_jwt_identity()
        user = storage.filter_one("User", id=user_id)
        tracking = [track.to_dict() for track in user.tracking]
        if tracking is None:
            return jsonify([])
        return jsonify([track.to_dict() for track in user.tracking]), 200
