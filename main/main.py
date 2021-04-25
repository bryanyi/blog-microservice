import os
from dotenv import load_dotenv
from flask_cors import CORS
load_dotenv()
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config("SQLALCHEMY_DATABASE_URI") = os.getenv("SQL_ALCHEMY")
CORS(app)

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)

@app.route('/')
def index():
    return 'hello from flask! =)'

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')