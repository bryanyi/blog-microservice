import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import UniqueConstraint
# from dotenv import load_dotenv
# load_dotenv()

app = Flask(__name__)
# CONNECTING TO DATABASE
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('SQLALCHEMY_URI')
CORS(app)

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))
    
class ProductUser(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    
    # COMBINATION OF USER_ID AND PRODUCT_ID SHOULD STAY UNIQUE & NOT REPEATED
    UniqueConstraint('user_id', 'product_id', name='user_product_unique')
    
    

@app.route('/')
def index():
    return 'Helloooo!!!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

