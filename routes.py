from flask import Blueprint, request, jsonify, render_template, redirect, flash
from controllers import get_expenses, get_expense, create_expense, update_expense, delete_expense

bp = Blueprint('expenses', __name__)

@bp.route('/')
def app_init():
    expenses = get_expenses()
    return render_template('index.html', title="Página Inicial", expenses=expenses)

@bp.route('/expenses', methods=['GET'])
def list():
    expenses = get_expenses()
    return jsonify([{
        'id': e.id,
        'description': e.description,
        'value': e.value,
        'date': e.date,
        'paid': e.paid
    } for e in expenses])

@bp.route('/expenses', methods=['POST'])
def add():
    description = request.form['description']
    value = request.form['value']
    if description and value:
        expense = create_expense(description, value)
        return redirect('/')
    return jsonify({'message': 'Invalid data'}), 400

@bp.route('/expenses/<string:id>', methods=['GET'])
def fetch(id):
    expense = get_expense(id)
    if expense:
        return jsonify({
            'id': expense.id,
            'description': expense.description,
            'value': expense.value,
            'date': expense.date.isoformat(),
            'paid': expense.paid

        }), 200
    return jsonify({'message': 'Not found'}), 404

@bp.route('/expenses/<string:id>', methods=['PATCH'])
def patch(id):
    data = request.get_json()
    description = data.get('description')
    value = data.get('value')
    date = data.get('date')
    paid = data.get('paid')
    if description and value:
        update_expense(id, description, value, paid)
        return jsonify({
            'id': id,
            'description': description,
            'value': value,
            'date': date,
            'paid': paid
        }), 200, redirect('/')
    return jsonify({'message': 'Not found'}), 404

@bp.route('/expenses/delete/<string:id>', methods=['POST'])
def delete(id):
    expense = delete_expense(id)
    if request.form.get('_method') == 'DELETE' and expense:
        return redirect('/')
    return jsonify({'message': 'Not found'}), 404