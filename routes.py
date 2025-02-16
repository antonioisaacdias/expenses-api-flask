from flask import Blueprint, request, jsonify, abort
from controllers import get_expenses, get_expense, create_expense, update_expense, delete_expense

bp = Blueprint('expenses', __name__)

@bp.route('/', methods=['GET'])
def app_init():
    return 'Bem vindo!'

@bp.route('/expenses', methods=['GET'])
def list():
    expenses = get_expenses()
    return jsonify([{
        'id': e.id,
        'description': e.description,
        'value': e.value,
        'date': e.date
    } for e in expenses])

@bp.route('/expenses', methods=['POST'])
def add():
    expenseData = request.get_json()
    description = expenseData.get('description')
    value = expenseData.get('value')
    if description and value:
        expense = create_expense(description, value)
        return jsonify({
            'id': expense.id,
            'description': expense.description,
            'value': expense.value,
            'date': expense.date
        }), 201
    return jsonify({'message': 'Invalid data'}), 400

@bp.route('/expenses/<string:id>', methods=['GET'])
def fetch(id):
    expense = get_expense(id)
    if expense:
        return jsonify({
            'id': expense.id,
            'description': expense.description,
            'value': expense.value,
            'date': expense.date.isoformat()
        }), 200
    return jsonify({'message': 'Not found'}), 404

@bp.route('/expenses/<string:id>', methods=['PATCH'])
def patch(id):
    data = request.get_json()
    description = data.get('description')
    value = data.get('value')
    date = data.get('date')
    if description and value:
        update_expense(id, description, value)
        return jsonify({
            'id': id,
            'description': description,
            'value': value,
            'date': date
        }), 200
    return jsonify({'message': 'Not found'}), 404