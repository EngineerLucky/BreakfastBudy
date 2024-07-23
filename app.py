from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///menu.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Menu Model
class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(200), nullable=True)

# Create the database
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu', methods=['GET'])
def get_menu():
    menu_items = MenuItem.query.all()
    return jsonify([item.as_dict() for item in menu_items])

@app.route('/menu', methods=['POST'])
def add_menu_item():
    data = request.get_json()
    new_item = MenuItem(
        name=data['name'],
        description=data['description'],
        price=data['price'],
        image_url=data['image_url']
    )
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.as_dict()), 201

@app.route('/menu/<int:item_id>', methods=['PUT'])
def update_menu_item(item_id):
    data = request.get_json()
    item = MenuItem.query.get(item_id)
    if item:
        item.name = data['name']
        item.description = data['description']
        item.price = data['price']
        item.image_url = data['image_url']
        db.session.commit()
        return jsonify(item.as_dict())
    else:
        return jsonify({'error': 'Item not found'}), 404

@app.route('/menu/<int:item_id>', methods=['DELETE'])
def delete_menu_item(item_id):
    item = MenuItem.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
        return jsonify({'message': 'Item deleted'})
    else:
        return jsonify({'error': 'Item not found'}), 404

# Helper method to serialize data
def to_dict(self):
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}
MenuItem.as_dict = to_dict

if __name__ == '__main__':
    app.run(debug=True)

