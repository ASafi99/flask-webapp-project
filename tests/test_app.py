import unittest 
from flask_testing import TestCase
from flask import url_for, request

from application import app, db
from application.models import Users, Transactions

class TestBase (TestCase):

    def create_app (self): 
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
        TESTING = True,
        WTF_CSRF_ENABLED = False)

        return app 

    def setUp (self): 
        db.create_all()
        
        self.new_user = Users(name = "John", email = "John@gmail.com", wallet = 240 )
        self.new_expense = Transactions(date = "2021-12-22", 
                                amount = 10, 
                                paytype = "Cash",
                                category = "Travel",
                                notes= "travel for work",
                                expense_userid = 1) 
        db.session.add (self.new_user)
        db.session.add (self.new_expense)
        
        db.session.commit()

        
 
    def tearDown (self):
        db.session.remove()
        db.drop_all()

class TestAccess (TestBase): 
    def test_access_users (self): 
        response = self.client.get(url_for("User_page"))
        self.assertEqual (response.status_code, 200)
    def test_access_show_expenses (self): 
        response = self.client.get (url_for("Transaction"))
        self.assertEqual (response.status_code, 200)


class TestNoUser (TestBase): 

    def test_find_user(self): 
        
        response = self.client.get (url_for("User_page"))
        self.assertIn(b'John', response.data)
    

class Test_Show_Expenses (TestBase): 

    def test_expenses(self): 
        
        response = self.client.get("/expenses?userid=1&name=John") 
        self.assertIn(b'travel for work', response.data)

    def test_greeting(self): 
        
        response = self.client.get("/expenses?userid=1&name=John") 
        self.assertIn(b'Hello, John', response.data)

    def test_total_amount(self): 
        
        response = self.client.get("/expenses?userid=1&name=John") 
        self.assertIn(b'Total Expended Amount (\xc2\xa3): 10', response.data)

class Test_Add_Expenses (TestBase): 

    def test_add_new_expense(self): 
        
        response = self.client.get ("/expenses?userid=1&name=John") 
        self.assertIn(b'Add Expense', response.data)
    
class Test_Update_Expenses (TestBase): 

    def test_delete_expense(self): 
        
        response = self.client.get("/expenses?userid=1&name=John")
        self.assertIn(b'Delete', response.data)

    def test_update_expense(self): 
        
        response = self.client.post("/delete/1/")
        response1 = self.client.get ("/expenses?userid=1&name=John") 
        self.assertIn(b'Expense Deleted Successfully', response1.data)
        
class Test_Post_User (TestBase): 

    def test_post_user(self): 
        response = self.client.post ((url_for("addUser")),
                                    data = dict(name = "Jane", email = "jane@gmail.com",
                                    wallet=20),
                                    follow_redirects=True)
        self.assertIn(b'Jane', response.data)


class Test_Post_New_Expenses (TestBase): 

    def test_post_new_expenses(self): 
        response = self.client.post ((url_for("addTransaction")),
                                    data = dict(
                                date = "2021-12-25", 
                                amount = 20, 
                                paytype = "Cash",
                                category = "Groceries",
                                notes= "Groceries for Jane",
                                expense_userid = 2), 
                                    follow_redirects=True)
        self.assertIn(b'Bad Request', response.data)