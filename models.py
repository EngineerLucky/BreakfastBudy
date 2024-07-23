from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(200), nullable=True)

def to_dict(self):
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}

MenuItem.as_dict = to_dict

