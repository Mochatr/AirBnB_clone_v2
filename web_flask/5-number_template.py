#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template


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


@app.route("/python/", defaults={"username": ""}, strict_slashes=False)
@app.route("/python/<username>", strict_slashes=False)
def print_python_path(username):
    """ Display python path """
    if username == "":
        return "Python is cool"

    return "Python {}".format(username.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def print_integer(n):
    """ Display number if it is an integer """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def render_number(n):
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
