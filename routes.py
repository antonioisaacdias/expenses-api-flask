from flask import Blueprint, request, jsonify
from controllers import get_expenses, get_expense, create_expense, update_expense, delete_expense

bp = Blueprint('expenses', __name__)

@bp.route('/', methods=['GET'])
def app_init():
    return 'Bem vindo!'

@bp.route('/expenses', methods=['GET'])
def list_expenses():
    expenses = get_expenses()
    return jsonify([{
        'id': e.id,
        'description': e.description,
        'value': e.value,
        'date': e.date
    } for e in expenses])

@bp.route('/expenses', methods=['POST'])
def add_expense():
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