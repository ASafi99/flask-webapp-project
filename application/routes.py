from flask import render_template, request, redirect, session,url_for, session
from flask.helpers import flash
from application.models import Transactions, Users
from application import app,db

@app.route('/expenses')
def Transaction(): 
    name_user = request.values.get("user")
    expenses_user = Transactions.query.all()
    # all_data = Transactions.query.all()
    return render_template("expenses.html", expenses = expenses_user,isUsers=False)

@app.route('/addExpenses',methods=['POST'])
def addTransaction():

    # name_user = request.values.get("user")
    
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
    return redirect(url_for('Transactions'))

@app.route('/')
@app.route('/users')
def User_page(): 
    all_users = Users.query.all()
    return render_template("users.html", all_users = all_users, isUsers=True)

@app.route('/addUsers',methods=['POST'])
def addUser(): 
    name = request.form['name']
    email = request.form['email']
    wallet = request.form['wallet']
    
    my_data = Users(name,email,wallet)

    db.session.add(my_data)
    db.session.commit()

    print(name +  " " + email + " " + wallet )

    flash('User has been successfully added!')

    return redirect(url_for('User_page'))

# @app.route('/update', methods = ['GET', 'POST'])
# def update():
 
#     if request.method == 'POST':
#         my_data = Data.query.get(request.form.get('id'))
 
#         my_data.name = request.form['name']
#         my_data.email = request.form['email']
#         my_data.phone = request.form['phone']
 
#         db.session.commit()
#         flash("Employee Updated Successfully")
 
#         return redirect(url_for('Index'))    

