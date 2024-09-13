#!/usr/bin/python3
""" registration and login authentication """
from models.users import User
from models import storage
from api.v1.views import api_v1
from flask import jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token



@api_v1.route('/signup', methods=['POST', 'GET'], strict_slashes=False)
def signup():
    data = request.get_json()
    if data is None:
        return jsonify({"message": "No input data provided"}), 400
    
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    phoneNumber = data.get('phoneNumber')
    address = data.get('address')
    email = data.get('email')
    password = data.get('password')
    
    if storage.filter_one("User", email=email):
        return jsonify({"error": "User already exists"}), 400
        

    new_user = User(first_name=first_name,last_name=last_name, phoneNumber=phoneNumber, address=address,email=email, password=password)
    new_user.save()
    return jsonify({"message": "User registered successfully"}), 201

@api_v1.route('/login', methods=['POST', 'GET'], strict_slashes=False)
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = storage.filter_one("User", email=email)
    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)
    return jsonify(access_token=access_token, refresh_token=refresh_token), 200