from flask import Blueprint, request, jsonify, render_template, redirect, flash
from controllers import get_expenses, get_expense, create_expense, update_expense, delete_expense


bp = Blueprint('expenses', __name__)

@bp.route('/')
def app_init():
    expenses = get_expenses()
    return render_template('expenses-table.html', title="Página Inicial", expenses=expenses)

@bp.route('/expenses', methods=['POST'])
def add():
    description = request.form['description']
    value = request.form['value']
    category = request.form['category']
    dueAt = request.form['dueAt']
    if description and value:
        create_expense(description, value, category, dueAt)
        return redirect('/')
    return jsonify({'message': 'Invalid data'}), 400

@bp.route('/expenses/<string:id>', methods=['GET'])
def fetch(id):
    expense = get_expense(id)
    if expense:
        return render_template('update-expense.html', title="Edição de Despesa", expense=expense)
    return jsonify({'message': 'Not found'}), 404

@bp.route('/expenses/update/<string:id>', methods=['POST'])
def update(id):
    description = request.form.get('description')
    value = request.form.get('value')
    paidAt = True if request.form.get('paidAt') else False
    update_expense(id, description, value, paidAt)
    return redirect('/')

@bp.route('/expenses/delete/<string:id>', methods=['POST'])
def delete(id):
    expense = delete_expense(id)
    if request.form.get('_method') == 'DELETE' and expense:
        return redirect('/')
    return jsonify({'message': 'Not found'}), 404