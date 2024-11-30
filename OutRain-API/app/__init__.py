from flask import Flask

def create_app():
    app = Flask(__name__)
    from .api import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/v1/api')
    return app
