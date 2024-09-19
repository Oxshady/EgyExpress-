from flask import Blueprint


api_v1 = Blueprint('api_v1', __name__, url_prefix='/api')

from api.v1.views.users import *
from api.v1.views.orders import *
from api.v1.views.cart import *
from api.v1.views.category import *
from api.v1.views.subcategory import *
from api.v1.views.Reviews import *
from api.v1.views.authentication import *
from api.v1.views.refresh import *
from api.v1.views.product import *