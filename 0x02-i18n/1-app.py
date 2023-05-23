#!/usr/bin/env python3
""" Basic Flask app """

from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """ Config class for Babel object """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


# list of routes of my app


@app.route('/', strict_slashes=False)
def index():
    """ Returns: 1-index.html """
    header = "Hello world"
    return render_template('1-index.html', header=header)


if __name__ == '__main__':
    """ Main Function"""
    app.run()
