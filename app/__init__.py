from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['*'])
app.config['CORS_HEADERS'] = 'Content-Type'

from app.signup import routes
from app.login import routes
from app.family import routes
from app.actions import routes
from app.family_account_type import routes
from app.targets import routes