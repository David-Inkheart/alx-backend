#!/usr/bin/env python3
""" Basic Flask app """

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

# list of routes of my app


@app.route('/', strict_slashes=False)
def index():
    """ Returns: 0-index.html """
    header = "Hello world"
    return render_template('0-index.html', header=header)


if __name__ == '__main__':
    """ Main Function"""
    app.run()
