from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import uuid

app = Flask(__name__,
static_url_path='/flask-webapp-project/application/static', 
template_folder='templates'
)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SECRET_KEY'] = str(uuid.uuid4()) # generating a random secret key at app startup
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

db = SQLAlchemy(app)
from application import routes
