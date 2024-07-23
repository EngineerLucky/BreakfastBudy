from flask import Flask
from flask_jwt_extended import JWTManager
from .models import db, bcrypt
from .config import Config
from .routes import bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    JWTManager(app)

    app.register_blueprint(bp)

    with app.app_context():
        db.create_all()

    return app

