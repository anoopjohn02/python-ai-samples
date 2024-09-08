"""
Server routes
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    """
    Hello world route!!!
    """
    return "Hello World"
