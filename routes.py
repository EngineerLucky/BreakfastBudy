from flask import Blueprint, request, jsonify, render_template
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from .models import db, User, MenuItem, bcrypt

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/menu', methods=['GET'])
def get_menu():
    menu_items = MenuItem.query.all()
    return jsonify([item.as_dict() for item in menu_items])

@bp.route('/menu', methods=['POST'])
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

@bp.route('/menu/<int:item_id>', methods=['PUT'])
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

@bp.route('/menu/<int:item_id>', methods=['DELETE'])
def delete_menu_item(item_id):
    item = MenuItem.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
        return jsonify({'message': 'Item deleted'})
    else:
        return jsonify({'error': 'Item not found'}), 404

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity={'username': user.username})
        return jsonify({'access_token': access_token}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

@bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({'message': f'Hello, {current_user["username"]}'}), 200

