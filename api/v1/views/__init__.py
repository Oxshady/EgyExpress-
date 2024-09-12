from flask import Blueprint

api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')

from api.v1.views.users import *
from api.v1.views.orders import *