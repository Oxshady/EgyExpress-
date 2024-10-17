#!/usr/bin/python3
""" shows user info on the profile page and allow for editing these info and logout and delete user acc """
from models.users import User
from models import storage
from api.v1.views import api_v1
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required


@api_v1.route('/profile', methods=['GET'], strict_slashes=False)
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    user = storage.get("User",id=user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 405
    
    user_info = {
        'id': user.id,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'phone_number': user.phoneNumber,
        'address': user.address
    }
    
    return jsonify(user_info), 200


@api_v1.route('/profile/edit', methods=['PUT', 'POST'], strict_slashes=False)
@jwt_required()
def edit_profile():
    user_id = get_jwt_identity()
    user = storage.get("User",id=user_id)

    if not user:
        return jsonify({'error': 'User not found'}), 404

    try:
        data = request.get_json()
        if not isinstance(data, dict):
            raise ValueError("Invalid JSON data")
    except Exception as e:
        return jsonify({'error': 'Invalid request data'}), 400

    if  "old_password" in data:
        old_password = data['old_password']
        if not user.check_password(old_password):
            return jsonify({"error": "wrong password"}), 402
        if data['new_password']:
            new_password = data['new_password']
            new_password = user.hash_password(new_password)
            setattr(user, 'password', new_password)

    else:
        for attr, value in data.items():
            setattr(user, attr, value)

    user.save()

    return jsonify({'message': 'Profile updated successfully'}), 200


@api_v1.route('/profile/logout', methods=['POST'])
@jwt_required()
def logout_user():
    user_id = get_jwt_identity()
    
    user = storage.get("User",id=user_id)

    response = jsonify({
        'msg': f'Logged out successfully. See you later, {user.name}!'
    })
    
    return response, 200


@api_v1.route('/profile/delete', methods=['DELETE'])
@jwt_required()
def delete_profile():
    user_id = get_jwt_identity()
    
    user = storage.get("User",id=user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    user.delete()

    return jsonify({'message': 'User account deleted successfully'}), 200
