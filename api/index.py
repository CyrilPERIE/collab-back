from flask import Flask
from flask_cors import cross_origin

app = Flask(__name__)

@app.route('/')
@cross_origin()
def home():
    return 'Hello, World!'

@app.route('/health-check')
def health_check():
    return 'RUNNING!'