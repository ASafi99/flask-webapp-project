from flask import render_template, request, redirect, session,url_for, session
from flask.helpers import flash
from application.models import Transactions, Users
from application import app,db

@app.route('/')
@app.route('/users')
def User_page(): 
    count_users = Users.query.count()
    if count_users==0: 
        return render_template("users.html")
    else: 
        all_users = Users.query.all()
        return render_template("users.html", all_users = all_users)

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

@app.route('/expenses')
def Transaction(): 
    userid = request.values.get("userid")
    user_name = request.values.get("name")

    if userid ==None: 
        return redirect (url_for("User_page"))
    else: 
        expenses_user = db.session.query(Transactions).join(Users).filter(Users.id ==userid).all()
       

        if expenses_user==[]: 
            return render_template("expenses.html", name_user = user_name, userid=userid)
        else: 
            query = Transactions.query.filter (Transactions.expense_userid== userid).all()

            Total_amount = 0
            for data in query: 
                data.amount
                Total_amount +=data.amount
            total_amount = round(Total_amount,2)

            return render_template("expenses.html", expenses=expenses_user, name_user = user_name, userid=userid, total =total_amount) 

@app.route('/addExpenses',methods=['POST'])
def addTransaction():

    userid = request.form["id"]
  
    
    date = request.form['date']
    amount = request.form['amount']
    paytype = request.form['paytype']
    category = request.form['category']
    notes = request.form['notes']
    
    my_data = Transactions(date,amount,paytype,category,notes,userid)
    db.session.add(my_data)
    db.session.commit()
    print(date +  " " + amount + " " + paytype + " " + category)

    flash('Transaction has been successfully added!')
    return redirect(url_for('Transaction'))


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

