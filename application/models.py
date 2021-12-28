from datetime import datetime
from application import app, db

class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.String(100))
    amount = db.Column(db.Integer())
    paytype = db.Column(db.String(100))
    category = db.Column(db.String(100))
    notes = db.Column(db.String(100))
 
 
    def __init__(self,date, amount,paytype,category,notes):
 
        self.date = date
        self.amount = amount
        self.paytype= paytype
        self.category= category
        self.notes= notes
