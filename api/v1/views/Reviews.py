from api.v1.views import api_v1
from flask import jsonify, request
from models import storage
from models.Review import Review
@api_v1.route('/reviews', methods=['GET', 'POST'])
def reviews():
    """ reviews endpoint """
    if request.method == 'GET':
        reviews = storage.get_all("Review")
        if reviews is None:
            return jsonify([])
        return jsonify([review.to_dict() for review in reviews])
    elif request.method == 'POST':
        data = request.get_json()
        user = storage.get_all("User")[0]
        rate = data.get('rate')
        description = data.get('description')
        product = storage.get_all("Product")[0]
        product_id = product.id
        review = Review(rate=rate, description=description, user=user, product=product)
        storage.post(review)
        return jsonify({"success":True}), 201