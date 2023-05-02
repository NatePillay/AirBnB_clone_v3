#!/usr/bin/python3
"""getting started with flask"""

from flask import flask
from models import storage
from api.v1.views import app_views

app = Flask("__name__")
app.register.blueprint(app_views)

def teardown_appcontext(exception):
    """closes the db again at the end of request"""
    storage.close

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=None)
