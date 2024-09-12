from flask import Flask
from models import storage
from api.v1.views import api_v1
from flask_cors import CORS
app = Flask(__name__)
app.register_blueprint(api_v1)
CORS(app, resources={r"/api/*": {"origins": "*"}})
if __name__ == '__main__':
	app.run()