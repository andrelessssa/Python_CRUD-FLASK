from flask import Blueprint, request, jsonify
from models import db, Item

api = Blueprint('api', __name__)

@api.route('/itens', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = Item(name=data['name'], description=data.get('description'))
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'message': 'Item created'}), 201
