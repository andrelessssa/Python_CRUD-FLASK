from flask import Flask
from config import Config
from models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    @app.route('/')
    def index():
        return 'Hello, World!'
    
    with app.app_context():
        db.create_all()

    return app    