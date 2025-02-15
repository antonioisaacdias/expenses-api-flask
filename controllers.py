from models import Expense
from database import db

def get_expenses():
    return Expense.query.all()

def get_expense(id):
    return Expense.query.get(id)

def create_expense(description, value):
    expense = Expense(description=description, value=value)
    db.session.add(expense)
    db.session.commit()
    return expense

def update_expense(id, description, value):
    expense = Expense.query.get(id)
    if expense:
        expense.description = description
        expense.value = value
        db.session.commit()
        return expense
    
def delete_expense(id):
    expense = Expense.query.get(id)
    if expense:
        db.session.delete(expense)
        db.session.commit()
        return True
    return False