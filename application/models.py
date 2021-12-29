from datetime import datetime

from sqlalchemy.orm import backref
from application import app, db

class Users(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key = True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120))
    wallet = db.Column(db.Integer())
    # expenses = db.relationship('Transactions', backref='users')
    
    def __init__(self,name,email,wallet):
        self.name = name
        self.email = email
        self.wallet = wallet
        


class Transactions(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key = True)
    date = db.Column(db.String(100))
    amount = db.Column(db.Integer())
    paytype = db.Column(db.String(100))
    category = db.Column(db.String(100))
    notes = db.Column(db.String(100))
    # expense_userid = db.Column(db.Integer, db.ForeignKey('users.name'))
 
 
    def __init__(self,date, amount,paytype,category,notes):
 
        self.date = date
        self.amount = amount
        self.paytype= paytype
        self.category= category
        self.notes= notes
        # self.expense_userid = expense_userid

