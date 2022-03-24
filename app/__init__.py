from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run()

from app.paybox_client import routes
from app.login import routes
