#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def states():
    """ Get all state data """
    states = storage.all("State")
    return render_template("9-states.html", states=states)


@app.route('/states')
def cities_by_states(id):
    """ Get all state data """
    states = storage.all("State")
    state_id = "state." + id

    if state_id in states.key():
        return render_template("9-states.html",
                               states=states[state_id], id=id)
    
    return render_template("9-states.html", not_found="not found")


@app.teardown_appcontext
def terminate(exc):
    """ Close SQLAlchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
