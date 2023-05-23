#!/usr/bin/env python3
""" Basic Flask app """

from typing import Union
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
def get_locale() -> Union[str, None]:
    """ get locale from request and return best match"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """ Returns: 3-index.html """
    return render_template('3-index.html')


if __name__ == '__main__':
    """ Main Function"""
    app.run()
