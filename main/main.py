import os
from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
load_dotenv()
from sqlalchemy import UniqueConstraint
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQL_ALCHEMY")
CORS(app)

db = SQLAlchemy(app)

@dataclass
class Product(db.Model):
    id: int
    title: str
    image: str
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

@dataclass    
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    
    UniqueConstraint('user_id', 'product_id', name='user_product_unique')


@app.route('/')
def index():
    return 'hello from flask! =)'

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')