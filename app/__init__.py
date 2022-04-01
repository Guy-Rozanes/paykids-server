from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['*'])
app.config['CORS_HEADERS'] = 'Content-Type'

from app.signup import routes
from app.login import routes
from app.family import routes