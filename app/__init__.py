from flask import Flask
from app.routes import api
from app.web_routes import web

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(web)
    return app
