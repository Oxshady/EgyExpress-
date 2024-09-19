from flask import Flask
from models import storage
from api.v1.views import api_v1
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from datetime import timedelta
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = '7809b82167fe37c83af13486f17903a873ea5e9b4a244253'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=365 * 5)
jwt = JWTManager(app)
app.register_blueprint(api_v1)
CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.teardown_appcontext
def close(exception=None):
    if exception:
        storage.roll()
    else:
        storage.save()
    storage.close()

if __name__ == '__main__':
    app.run() 

