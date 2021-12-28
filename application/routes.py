from flask import render_template, request, redirect, session,url_for
from flask.helpers import flash
from application.models import Transactions
from application import app,db

@app.route('/')
def Index(): 
    all_data = Transactions.query.all()
    return render_template("index.html", expenses = all_data)

@app.route('/add',methods=['POST'])
def addTransaction():
    
    date = request.form['date']
    amount = request.form['amount']
    paytype = request.form['paytype']
    category = request.form['category']
    notes = request.form['notes']
    
    my_data = Transactions(date,amount,paytype,category,notes)
    db.session.add(my_data)
    db.session.commit()
    print(date +  " " + amount + " " + paytype + " " + category)

    flash('Transaction has been successfully added!')
    return redirect(url_for('Index'))

