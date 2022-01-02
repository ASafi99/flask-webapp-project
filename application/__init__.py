from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import uuid

app = Flask(__name__,
static_url_path='/flask-webapp-project/application/static', 
template_folder='templates'
)

# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password@expense_database:3306/expense"
app.config['SECRET_KEY'] = str(uuid.uuid4()) # generating a random secret key at app startup

db = SQLAlchemy(app)
from application import routes
