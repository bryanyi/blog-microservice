from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config()

@app.route('/')
def index():
    return 'hello from flask! =)'

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')