#!/usr/bin/env python3
""" Basic Flask app """

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config(object):
    """ Config class for Babel object """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ get locale from request """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# the decorator to mark the function get_locale as a local selector
# does not work with later versions of Flask-Babel so the following is used
# babel.init_app(app, locale_selector=get_locale)


# list of routes of my application
@app.route('/', strict_slashes=False)
def index():
    """ Returns: 3-index.html """
    return render_template('3-index.html')


if __name__ == '__main__':
    """ Main Function"""
    app.run()
