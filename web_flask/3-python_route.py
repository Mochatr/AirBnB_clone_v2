#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """ Display Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Display HBNB """
    return "HBNB"


@app.route("/c/<username>", strict_slashes=False)
def print_path(username):
    """ Display C path """
    return "C {}".format(username.replace("_"," "))


@app.route("/python/", defaults={"text": ""}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def print_python_path(text):
    """ Display python path """
    if text == "":
        return "Python is cool"

    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
