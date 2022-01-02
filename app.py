from application import app, db
from application.models import Users


if __name__ == "__main__":
    app.run(host = '0.0.0.0',debug=True)