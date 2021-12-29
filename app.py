from application import app, db
from application.models import Users

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)